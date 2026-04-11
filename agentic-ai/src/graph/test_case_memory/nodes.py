import json
from pathlib import Path
import pandas as pd
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from src.core import search_vector_store, PersistentMemory

from .state import TestCaseState
from src.core import get_langchain_llm, pick_requirement, get_logger
from src.prompts.testcase_prompts import TESTCASE_SYSTEM_PROMPT

persistent_memory = PersistentMemory(collection_name="test_cases_memory")

logger = get_logger("testcase_graph")
ROOT = Path(__file__).resolve().parents[3]
REQ_DIR = ROOT / "data" / "requirements"
OUT_DIR = ROOT / "outputs" / "testcase_rag"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Build Langchain components
llm = get_langchain_llm()
prompt_template = ChatPromptTemplate.from_messages([
    ("system", TESTCASE_SYSTEM_PROMPT),
    ("user", "Requirements:\n\n{requirement}")
])
parser = StrOutputParser()
chain = prompt_template | llm | parser

def read_requirement(state: TestCaseState) -> TestCaseState:
    if state.get("requirement"):
        if state.get("conversation_history"):
            # Actual Follow up conversation.
            print(f"Follow up Instructions: {state['requirement'][:60]}")
        else:
            # Actual Requirement passed via CLI
            print(f"Requirement loaded from the file")
        return {}
    req_file = pick_requirement(None, REQ_DIR)
    requirementOuput = req_file.read_text(encoding="utf-8")
    return {"requirement": requirementOuput}

def generate_tests(state: TestCaseState) -> TestCaseState:
    """Generate test cases using RAG + STM + LTM context."""
    requirement = state["requirement"]
    retrieved_context = state.get("retrieved_context", "")
    past_patterns = state.get("past_patterns", "")  # Long term memory
    conversation_history = state.get("conversation_history", []) # Short term memory
    existing_test_cases = state.get("test_cases", [])  # restored from checkpoint by MemorySaver

    # Build conversation context from STM (last 6 messages)
    conversation_text = ""
    if conversation_history:
        lines = [f"{msg['role']}: {msg['content']}" for msg in conversation_history[-6:]]
        conversation_text = "\n".join(lines)

    # Compose prompt — three context sources + requirement
    user_message = f"""COMPANY TESTING GUIDELINES:
{retrieved_context}
"""
    if past_patterns:
        user_message += f"""
PAST TEST CASE PATTERNS (from previous sessions):
{past_patterns}
"""

    if conversation_history and existing_test_cases:
        # Follow-up mode — LLM must ADD to existing test cases, not regenerate
        existing_json = json.dumps(existing_test_cases, indent=2)
        user_message += f"""
CONVERSATION HISTORY (current session):
{conversation_text}

EXISTING TEST CASES (already generated in this session):
{existing_json}

FOLLOW-UP INSTRUCTION: {requirement}
Add the requested test cases to the existing list above.
Return ALL test cases (existing + new ones) as a single JSON array.
Do NOT regenerate existing ones — only append new ones with the next available TC IDs.
"""
    else:
        # First run — generate fresh
        user_message += f"""
REQUIREMENT:
{requirement}
"""

    try:
        response = chain.invoke({"requirement": user_message})
        testcases = json.loads(response)

        # Update STM — append this turn to conversation history
        updated_history = list(conversation_history)
        updated_history.append({"role": "user", "content": requirement})
        tc_ids = ", ".join(tc.get("id", "") for tc in testcases)
        updated_history.append({
            "role": "agent",
            "content": f"Generated {len(testcases)} test case(s): {tc_ids}"
        })

        return {
            "test_cases": testcases,
            "errors": [],
            "conversation_history": updated_history
        }

    except json.JSONDecodeError as e:
        return {"test_cases": [], "errors": [f"JSON parse error: {e}"]}
    except Exception as e:
        return {"test_cases": [], "errors": [f"LLM error: {e}"]}
  
def save_outputs(state: TestCaseState) -> TestCaseState:
    """Save test cases to files. LTM save happens in driver after user confirms."""
    from datetime import datetime
    test_cases = state["test_cases"]

    if not test_cases:
        return {}

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Save raw JSON — timestamped so sessions don't overwrite each other
    raw_file = OUT_DIR / f"raw_output_{timestamp}.txt"
    raw_file.write_text(json.dumps(test_cases, indent=2), encoding="utf-8")

    # Save CSV — timestamped
    df = pd.DataFrame(test_cases)
    if "steps" in df.columns:
        df["steps"] = df["steps"].apply(
            lambda x: " | ".join(x) if isinstance(x, list) else x
        )
    csv_file = OUT_DIR / f"test_cases_{timestamp}.csv"
    df.to_csv(csv_file, index=False)

    print(f"Saved {len(test_cases)} test cases to {OUT_DIR}")
    return {}


def validate_tests(state: TestCaseState) -> TestCaseState:
    """Validate generated test cases."""
    test_cases = state.get("test_cases", [])

    logger.info("Validating test cases...")

    # Validation checks
    if len(test_cases) < 3:
        logger.warning("Validation FAILED: Less than 3 test cases")
        return {"validation_status": "fail"}

    # Check each test case has required fields
    required_fields = ["id", "title", "steps", "expected", "priority"]
    for tc in test_cases:
        missing = [f for f in required_fields if f not in tc or not tc[f]]
        if missing:
            logger.warning(f"Validation FAILED: Missing fields {missing}")
            return {"validation_status": "fail"}

        # Check steps is a list with at least 2 steps
        if not isinstance(tc["steps"], list) or len(tc["steps"]) < 2:
            logger.warning("Validation FAILED: Steps must be list with 2+ items")
            return {"validation_status": "fail"}

    logger.info("✅ Validation PASSED")
    return {"validation_status": "pass"}

def retry_generate(state: TestCaseState) -> TestCaseState:
    """Retry test case generation."""
    retry_count = state.get("retry_count", 0) + 1
    logger.warning(f"🔄 Retry attempt {retry_count}/3")

    # Generate again (same logic as generate_tests)
    try:
        response = chain.invoke({"requirement": state["requirement"]})
        testcases = json.loads(response)
        logger.info(f"Regenerated {len(testcases)} test cases")

        return {
            "test_cases": testcases,
            "errors": [],
            "retry_count": retry_count,
            "validation_status": "pending"
        }

    except json.JSONDecodeError as e:
        logger.error(f"Failed to parse JSON: {e}")
        return {
            "test_cases": [],
            "errors": [f"JSON parse error: {e}"],
            "retry_count": retry_count,
            "validation_status": "fail"
        }
    except Exception as e:
        logger.error(f"LLM call failed: {e}")
        return {
            "test_cases": [],
            "errors": [f"LLM error: {e}"],
            "retry_count": retry_count,
            "validation_status": "fail"
        }

def route_after_validation(state: TestCaseState) -> str:
    """Decide next node based on validation result."""

    validation_status = state.get("validation_status", "pending")
    retry_count = state.get("retry_count", 0)

    # If passed validation → save
    if validation_status == "pass":
        logger.info("✅ Routing to SAVE")
        return "save"

    # If failed but can retry → retry
    if validation_status == "fail" and retry_count < 3:
        logger.warning(f"⚠️ Routing to RETRY (attempt {retry_count + 1}/3)")
        return "retry"

    # If max retries reached → save anyway
    logger.error("❌ Max retries reached, routing to SAVE")
    return "save"

def retrieve_context(state: TestCaseState) -> TestCaseState:
    """Retrieve relevant testing guidelines from knowledge base."""

    requirement = state["requirement"]
    logger.info("Retrieving relevant testing guidelines...")

    # Search vector store
    results = search_vector_store(
        query=f"test case guidelines for: {requirement[:200]}",
        top_k=3
    )

    # Format context
    context_parts = []
    for i, (doc, score) in enumerate(results, 1):
        source = doc.metadata.get('source', 'Unknown').split('/')[-1]
        similarity = 1 - score

        logger.info(f"Retrieved [{i}] {source} (similarity: {similarity:.2f})")

        context_parts.append(f"[Source: {source}]\\n{doc.page_content}\\n")

    retrieved_context = "\\n---\\n".join(context_parts)

    logger.info(f"Retrieved {len(results)} relevant documents")

    return {"retrieved_context": retrieved_context}


def load_memories(state: TestCaseState) -> TestCaseState:
    # Load the Short Term memory from the State and loading Long term memory from Chroma Db
    requirement = state["requirement"]
    conversation_history = state.get("conversation_history", []) # state["conversation_history"]"]
    
    # To Load the Short Term memory from the state -- restored automatically from the Memory Saver
    print(f"Loaded conversation history with {len(conversation_history)} interactions from Short Term Memory")
    
    # To Load the Long Term memory from the Chroma DB
    persistent_memory.get_context(
        query=f"test case patterns for {requirement[:200]}"
    )