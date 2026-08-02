"""
Pipeline Orchestrator.

Coordinates execution of all pipeline stages.

Author: Simba Munatsi
Project: PayFlow Intelligence Platform
"""

import time

from src.ingestion.history import PipelineHistory
from src.ingestion.loader import DataLoader
from src.utils.logger import get_logger

logger = get_logger(__name__)


class PipelineOrchestrator:

    def __init__(self):

        self.loader = DataLoader()

    def run(self):

        logger.info("=" * 60)
        logger.info("PAYFLOW INTELLIGENCE PIPELINE")
        logger.info("=" * 60)

        start = time.perf_counter()

        successful = 0
        failed = 0

        datasets = {}

        try:

            datasets, metadata, summary = self.loader.run()

            successful = summary.successful

            failed = summary.failed

            PipelineHistory.save(metadata)

        except Exception:

            logger.exception(
                "Landing Layer failed."
            )

            failed += 1

        duration = time.perf_counter() - start

        logger.info("-" * 60)
        logger.info(
            f"Pipeline completed in {duration:.2f} seconds"
        )

        logger.info(
            f"Successful datasets: {summary.successful}"
        )

        logger.info(
            f"Failed datasets: {summary.failed}"
        )

        if summary.failed:

            logger.warning(
                f"Failed dataset(s): "
                f"{', '.join(summary.failed_datasets)}"
            )
            
        logger.info("-" * 60)

        return datasets