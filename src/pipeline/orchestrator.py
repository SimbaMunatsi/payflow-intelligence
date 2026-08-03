"""
Pipeline Orchestrator.

Coordinates execution of all pipeline stages.

Author: Simba Munatsi
Project: PayFlow Intelligence Platform
"""

import time

from src.ingestion.history import PipelineHistory
from src.ingestion.loader import DataLoader
from src.transformation.staging import StagingEngine
from src.utils.logger import get_logger

logger = get_logger(__name__)


class PipelineOrchestrator:
    """
    Coordinates execution of all pipeline stages.

    Current Pipeline

    Raw
        ↓
    Landing
        ↓
    Staging

    Future Pipeline

    Raw
        ↓
    Landing
        ↓
    Staging
        ↓
    Validation
        ↓
    Warehouse
        ↓
    AI
    """

    def __init__(self):

        self.loader = DataLoader()

        self.staging_engine = StagingEngine()

    def run(self):

        logger.info("=" * 60)
        logger.info("PAYFLOW INTELLIGENCE PIPELINE")
        logger.info("=" * 60)

        start = time.perf_counter()

        datasets = {}

        staged_datasets = {}

        transformation_results = []

        successful = 0

        failed = 0

        summary = None

        try:

            # ==================================================
            # LANDING LAYER
            # ==================================================

            datasets, metadata, summary = self.loader.run()

            successful = summary.successful

            failed = summary.failed

            PipelineHistory.save(metadata)

            logger.info("Landing Layer completed successfully.")

            # ==================================================
            # STAGING LAYER
            # ==================================================

            staged_datasets, transformation_results = (
                self.staging_engine.run(
                    datasets
                )
            )

            logger.info("Staging Layer completed successfully.")

        except Exception:

            logger.exception(
                "Pipeline execution failed."
            )

            failed += 1

        duration = time.perf_counter() - start

        logger.info("-" * 60)

        logger.info(
            f"Pipeline completed in {duration:.2f} seconds"
        )

        if summary is not None:

            logger.info(
                f"Successful datasets : {summary.successful}"
            )

            logger.info(
                f"Failed datasets     : {summary.failed}"
            )

            if summary.failed:

                logger.warning(
                    "Failed dataset(s): "
                    + ", ".join(summary.failed_datasets)
                )

        logger.info(
            f"Transformation operations : "
            f"{len(transformation_results)}"
        )

        logger.info("-" * 60)

        return {
            "landing": datasets,
            "staging": staged_datasets,
            "transformation_results": transformation_results,
            "summary": summary,
            "duration_seconds": round(duration, 2),
        }