from src.core import build_vector_store, get_logger

logger = get_logger("build_index")

if __name__ == "__main__":
    logger.info("Building vector store...")
    try:
        vectore_store = build_vector_store()
    except Exception as e:
        logger.error(f"Failed to build vector store: {e}")
        raise