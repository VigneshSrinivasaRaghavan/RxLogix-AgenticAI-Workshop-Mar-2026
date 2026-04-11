"""
Log Analyzer - Graph Assembly
"""
from langgraph.graph import StateGraph, END
from .state import LogAnalyzerState
from .nodes import read_log, retrieve_context, analyze_log, save_outputs, load_memories
from langgraph.checkpoint.memory import MemorySaver

def build_graph():
    """Build and return compiled log analyzer graph."""

    # Create graph
    workflow = StateGraph(LogAnalyzerState)

    # Add nodes
    workflow.add_node("read", read_log)
    workflow.add_node("load_memories", load_memories)
    workflow.add_node("retrieve_context", retrieve_context)
    workflow.add_node("analyze", analyze_log)
    workflow.add_node("save", save_outputs)

    # Connect nodes
    workflow.set_entry_point("read")
    workflow.add_edge("read", "load_memories")
    workflow.add_edge("load_memories", "retrieve_context")
    workflow.add_edge("retrieve_context", "analyze")
    workflow.add_edge("analyze", "save")
    workflow.add_edge("save", END)

    # Compile
    checkpointer = MemorySaver()
    return workflow.compile(checkpointer=checkpointer)
