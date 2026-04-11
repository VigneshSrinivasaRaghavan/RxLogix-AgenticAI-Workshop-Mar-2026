"""
Log Analyzer with RAG - State Definition
"""
from typing import TypedDict, Dict, List

class LogAnalyzerState(TypedDict):
    """State for log analysis pipeline."""
    log_content: str
    retrieved_context: str      # NEW: Troubleshooting guides from vector store
    analysis_text: str
    analysis_json: Dict
    executive_summary: str
    errors: List[str]