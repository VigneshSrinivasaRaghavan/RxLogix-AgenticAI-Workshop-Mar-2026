import sys
from pathlib import Path
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from src.core import pick_requirement, get_logger, get_langchain_llm
from src.prompts import TESTCASE_SYSTEM_PROMPT

logger = get_logger("TestCaseLangChain")

# Project paths
ROOT = Path(__file__).resolve().parents[2]
REQ_DIR = ROOT / "data" / "requirements"
OUT_DIR = ROOT / "outputs" / "testcase_langchain"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Build Prompt Template
prompt_template = ChatPromptTemplate.from_messages([
    ("system", TESTCASE_SYSTEM_PROMPT),
    ("user", "{requirement}")
])

# Get LLM
llm = get_langchain_llm()

# Get parser
parser = JsonOutputParser()

# Build chain using LCEL(pipe operator)
chain = prompt_template | llm | parser

def main():
    # 1. Pick a requirement file
    file_arg = sys.argv[1] if len(sys.argv) > 1 else None
    req_file = pick_requirement(file_arg, REQ_DIR)
    requirement = req_file.read_text(encoding="utf-8")
    logger.info(f"Processing: {req_file.name}")
    
    # 2. Run the chain
    logger.info("Running LangChain chain...")
    testcases = chain.invoke({"requirement": requirement})
    
    # 3. Save outputs
    import json
    import pandas as pd

    # Save raw JSON
    raw_file = OUT_DIR / "raw_output_langchain.txt"
    raw_file.write_text(json.dumps(testcases, indent=2), encoding="utf-8")

    # Save CSV
    csv_file = OUT_DIR / "test_cases_langchain.csv"
    df = pd.DataFrame(testcases)
    df['steps'] = df['steps'].apply(lambda x: ' | '.join(x))
    df.to_csv(csv_file, index=False)

    # 4. Log results
    logger.info(f"Generated {len(testcases)} test cases")
    logger.info(f"Raw JSON: {raw_file.relative_to(ROOT)}")
    logger.info(f"CSV: {csv_file.relative_to(ROOT)}")
    logger.info("TestCase Agent (Langchain) completed")
    
if __name__ == "__main__":
    main()