from typing import TypedDict, Dict, List


class LogAnalyzerState(TypedDict):
    log_content: str
    user_instruction: str             # follow-up instruction typed in the driver loop
    conversation_history: List[Dict]  # STM — restored by MemorySaver between invocations
    past_incidents: str               # LTM — retrieved from ChromaDB at session start
    retrieved_context: str            # RAG — retrieved from troubleshooting guides
    analysis_text: str
    analysis_json: Dict
    executive_summary: str
    errors: List[str]