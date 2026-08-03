"""
Analytics Warehouse Builder.

Coordinates construction of the analytics warehouse.

Author: Simba Munatsi
Project: PayFlow Intelligence Platform
"""

from time import perf_counter

import pandas as pd

from src.analytics.warehouse.dimensions import (
    DimensionBuilder,
)
from src.analytics.warehouse.facts import (
    FactBuilder,
)
from src.analytics.warehouse.models import (
    WarehouseSummary,
)
from src.utils.logger import get_logger

logger = get_logger(__name__)


class WarehouseBuilder:
    """
    Builds the complete analytics warehouse.
    """

    def __init__(self):

        self.dimension_builder = (
            DimensionBuilder()
        )

        self.fact_builder = (
            FactBuilder()
        )

    def build(
        self,
        datasets: dict[str, pd.DataFrame],
    ):

        logger.info("=" * 60)
        logger.info("STARTING WAREHOUSE BUILD")
        logger.info("=" * 60)

        start = perf_counter()

        warehouse = {}

        all_results = []

        # ==========================================
        # Dimensions
        # ==========================================

        dimensions, dimension_results = (
            self.dimension_builder.build(
                datasets
            )
        )

        warehouse.update(dimensions)

        all_results.extend(
            dimension_results
        )

        # ==========================================
        # Facts
        # ==========================================

        facts, fact_results = (
            self.fact_builder.build(
                datasets
            )
        )

        warehouse.update(facts)

        all_results.extend(
            fact_results
        )

        duration = (
            perf_counter() - start
        )

        successful = sum(
            result.successful
            for result in all_results
        )

        failed = (
            len(all_results)
            - successful
        )

        summary = WarehouseSummary(

            total_tables=len(all_results),

            successful=successful,

            failed=failed,

            duration_seconds=duration,

            tables=all_results,

        )

        logger.info("=" * 60)
        logger.info("WAREHOUSE BUILD COMPLETE")
        logger.info("=" * 60)

        logger.info(
            f"Tables Built : {summary.total_tables}"
        )

        logger.info(
            f"Success Rate : {summary.success_rate}%"
        )

        return (

            warehouse,

            summary,

        )