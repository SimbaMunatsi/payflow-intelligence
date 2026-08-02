"""Entry point for running the pipeline."""

from src.ingestion.loader import load_data
from src.transformation.cleaning import clean_data
from src.transformation.standardization import standardize_data
from src.utils.logger import get_logger


def run_pipeline(path: str):
    """Run the ingestion and transformation pipeline."""
    logger = get_logger("pipeline")
    logger.info("Starting pipeline")
    data = load_data(path)
    cleaned = clean_data(data)
    standardized = standardize_data(cleaned)
    logger.info("Pipeline completed")
    return standardized


if __name__ == "__main__":
    run_pipeline("data/raw")
