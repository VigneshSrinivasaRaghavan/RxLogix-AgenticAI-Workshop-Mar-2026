import sys
from pathlib import Path
from typing import List, Dict
from src.core import chat, pick_requirement, parse_json_safely, get_logger
import pandas as pd

logger = get_logger("TestCaseAgent")

# Project Paths
ROOT = Path(__file__).resolve().parents[2]
REQ_DIR = ROOT / "data" / "requirements"
OUT_DIR = ROOT / "outputs" / "testcase_generated"
OUT_DIR.mkdir(parents=True, exist_ok=True)

SYSTEM_PROMPT = """You are a QA engineer. Generate test cases from requirements.

Return ONLY a JSON array with this structure:
[
  {
    "id": "TC-001",
    "title": "Short test title",
    "steps": ["Step 1", "Step 2", "Step 3"],
    "expected": "Expected result",
    "priority": "High"
  }
]

Rules:
- Return 5 test cases
- Cover positive and negative scenarios
- Include edge cases
- Keep steps clear and actionable
- Priority: High, Medium, or Low
- Return ONLY JSON, no markdown fences"""


def save_as_csv(test_cases: List[Dict], csv_file: Path) -> None:
    """Convert test cases to CSV using pandas."""

    rows = []
    for i, case in enumerate(test_cases, 1):
        # Extract fields with defaults
        test_id = case.get("id", f"TC-{i:03d}")
        title = case.get("title", "")
        expected = case.get("expected", "")
        priority = case.get("priority", "Medium")

        # Handle steps (list or string)
        steps = case.get("steps", [])
        if isinstance(steps, list):
            steps_text = " | ".join(steps)
        else:
            steps_text = str(steps)

        rows.append({
            "TestID": test_id,
            "Title": title,
            "Steps": steps_text,
            "Expected": expected,
            "Priority": priority
        })

    # Create DataFrame and save
    df = pd.DataFrame(rows)
    df.to_csv(csv_file, index=False, encoding="utf-8")


def main():
    # 1. Pick requirement file
    logger.info("Test Case Generator Agent Starting...")
    logger.debug("Picking requirement file...")
    file_arg = sys.argv[1] if len(sys.argv) > 1 else None
    req_file = pick_requirement(file_arg, REQ_DIR)
    requirement = req_file.read_text(encoding="utf-8")
    logger.info(f"Requirement file: {req_file}")
    
    # Build messages for LLM
    logger.debug("Generating test cases...")
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": requirement}
    ]
    
    logger.info("Sending messages to LLM...")
    response = chat(messages)
    logger.info("Test cases generated successfully!")
    
    raw_file = OUT_DIR / "raw_output.txt"
    
    testcases = parse_json_safely(response, raw_file)
    
    # Save as CSV
    csv_file = OUT_DIR / "test_cases.csv"
    save_as_csv(testcases, csv_file)
    
    logger.info(f"Test cases saved to {csv_file}")
    
if __name__ == "__main__":
    main()