"""
Driver for Log Analyzer Pipeline with RAG
"""
from src.graph.log_analyzer_rag.graph import build_graph
from src.core import get_logger

logger = get_logger("log_analyzer_rag_driver")

def main():
    logger.info("🚀 Starting Log Analyzer pipeline with RAG...")

    # Build graph
    app = build_graph()

    # Initialize state
    init_state = {
        "log_content": "",
        "retrieved_context": "",      # NEW
        "analysis_text": "",
        "analysis_json": {},
        "executive_summary": "",
        "errors": []
    }

    # Run pipeline
    final_state = app.invoke(init_state)

    # Show results
    logger.info(f"✅ Pipeline complete!")

    if final_state.get('errors'):
        logger.error(f"Errors: {final_state['errors']}")
    else:
        logger.info("Generated 3 reports: text, JSON, executive summary")

if __name__ == "__main__":
    main()
