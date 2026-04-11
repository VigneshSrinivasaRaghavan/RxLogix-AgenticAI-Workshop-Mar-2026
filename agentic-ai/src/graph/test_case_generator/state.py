from typing import TypedDict, List, Dict

class TestCaseState(TypedDict):
    requirement: str
    test_cases: List[Dict]
    errors: List[str]
    validation_status: str # New State - "pass" | "fail" | "pending"
    retry_count: int