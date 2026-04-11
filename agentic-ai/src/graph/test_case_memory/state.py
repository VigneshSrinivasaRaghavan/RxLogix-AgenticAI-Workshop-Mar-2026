from typing import TypedDict, List, Dict

class TestCaseState(TypedDict):
    requirement: str
    retrieved_context: str
    conversation_history: List[Dict]  # Short Term Memory
    past_patterns: str # Long Term Memory
    test_cases: List[Dict]
    errors: List[str]
    validation_status: str
    retry_count: int