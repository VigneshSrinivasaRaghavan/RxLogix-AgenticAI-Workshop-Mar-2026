import json
from pathlib import Path
import pandas as pd
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from src.core import search_vector_store

from .state import TestCaseState
from src.core import get_langchain_llm, pick_requirement, get_logger
from src.prompts.testcase_prompts import TESTCASE_SYSTEM_PROMPT

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
    req_file = pick_requirement(None, REQ_DIR)
    requirementOuput = req_file.read_text(encoding="utf-8")
    logger.info(f"Read requirement: {req_file.name}")
    return {"requirement": requirementOuput}

def generate_tests(state: TestCaseState) -> TestCaseState:
    """Generate test cases with RAG context."""
    logger.info("Generating test cases with RAG context...")

    requirement = state["requirement"]
    context = state.get("retrieved_context", "")

    # Build enhanced prompt with context
    user_message = f"""Based on the following company testing guidelines:

{context}

---

Now generate test cases for this requirement:

{requirement}"""

    try:
        response = chain.invoke({"requirement": user_message})
        testcases = json.loads(response)
        logger.info(f"Generated {len(testcases)} test cases using RAG")

        return {
            "test_cases": testcases,
            "errors": [],
            "retry_count": state.get("retry_count", 0),
            "validation_status": "pending"
        }

    except json.JSONDecodeError as e:
        logger.error(f"Failed to parse JSON: {e}")
        return {
            "test_cases": [],
            "errors": [f"JSON parse error: {e}"],
            "retry_count": state.get("retry_count", 0),
            "validation_status": "fail"
        }
    except Exception as e:
        logger.error(f"LLM call failed: {e}")
        return {
            "test_cases": [],
            "errors": [f"LLM error: {e}"],
            "retry_count": state.get("retry_count", 0),
            "validation_status": "fail"
        }
  
def save_outputs(state: TestCaseState) -> TestCaseState:
    """Save test cases to files."""
    test_cases = state["test_cases"]

    if not test_cases:
        logger.warning("No test cases to save")
        return {}

    # Save raw JSON
    raw_file = OUT_DIR / "raw_output.txt"
    raw_file.write_text(json.dumps(test_cases, indent=2), encoding="utf-8")
    logger.info(f"Saved raw JSON: {raw_file.relative_to(ROOT)}")

    # Save CSV
    df = pd.DataFrame(test_cases)
    if 'steps' in df.columns:
        df['steps'] = df['steps'].apply(lambda x: ' | '.join(x) if isinstance(x, list) else x)

    csv_file = OUT_DIR / "test_cases.csv"
    df.to_csv(csv_file, index=False)
    logger.info(f"Saved CSV: {csv_file.relative_to(ROOT)}")

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

