"""
Pipeline Orchestrator.

Coordinates execution of all pipeline stages.

Author: Simba Munatsi
Project: PayFlow Intelligence Platform
"""

import time

from src.analytics.warehouse.builder import WarehouseBuilder
from src.ingestion.history import PipelineHistory
from src.ingestion.loader import DataLoader
from src.transformation.staging import StagingEngine
from src.utils.logger import get_logger
from src.validation.validator import Validator

logger = get_logger(__name__)


class PipelineOrchestrator:
    """
    Coordinates execution of all pipeline stages.

    Pipeline Flow

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

        self.validator = Validator()

        self.warehouse_builder = WarehouseBuilder()

    def run(self):

        logger.info("=" * 60)
        logger.info("PAYFLOW INTELLIGENCE PIPELINE")
        logger.info("=" * 60)

        start = time.perf_counter()

        datasets = {}

        staged_datasets = {}

        warehouse = {}

        transformation_results = []

        validation_results = []

        validation_dashboard = None

        warehouse_summary = None

        summary = None

        try:

            # ==================================================
            # LANDING LAYER
            # ==================================================

            datasets, metadata, summary = (
                self.loader.run()
            )

            PipelineHistory.save(
                metadata
            )

            logger.info(
                "Landing Layer completed successfully."
            )

            # ==================================================
            # STAGING LAYER
            # ==================================================

            (
                staged_datasets,
                transformation_results,
            ) = self.staging_engine.run(
                datasets
            )

            logger.info(
                "Staging Layer completed successfully."
            )

            # ==================================================
            # VALIDATION LAYER
            # ==================================================

            (
                validation_results,
                validation_dashboard,
            ) = self.validator.validate_all(
                staged_datasets
            )

            logger.info(
                "Validation Layer completed successfully."
            )

            # ==================================================
            # WAREHOUSE LAYER
            # ==================================================

            (
                warehouse,
                warehouse_summary,
            ) = self.warehouse_builder.build(
                staged_datasets
            )

            logger.info(
                "Warehouse Layer completed successfully."
            )

        except Exception:

            logger.exception(
                "Pipeline execution failed."
            )

        duration = (
            time.perf_counter() - start
        )

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
                    + ", ".join(
                        summary.failed_datasets
                    )
                )

        logger.info(
            f"Transformation operations : "
            f"{len(transformation_results)}"
        )

        logger.info(
            f"Validation rules executed : "
            f"{len(validation_results)}"
        )

        if validation_dashboard:

            logger.info(
                f"Data Quality Score : "
                f"{validation_dashboard.quality_score}"
            )

        if warehouse_summary:

            logger.info(
                f"Warehouse tables built : "
                f"{warehouse_summary.total_tables}"
            )

            logger.info(
                f"Warehouse success rate : "
                f"{warehouse_summary.success_rate}%"
            )

        logger.info("-" * 60)

        return {

            "landing": datasets,

            "staging": staged_datasets,

            "transformation_results":
                transformation_results,

            "validation_results":
                validation_results,

            "validation_dashboard":
                validation_dashboard,

            "warehouse":
                warehouse,

            "warehouse_summary":
                warehouse_summary,

            "summary":
                summary,

            "duration_seconds":
                round(duration, 2),

        }