"""
Dashboard Service.

Builds the dashboard model consumed by the
FastAPI endpoints and Streamlit UI.

Author: Simba Munatsi
Project: PayFlow Intelligence Platform
"""

from datetime import datetime

from src.dashboard.models import (
    DashboardResponse,
    KPIModel,
    PipelineStage,
    PipelineStatus,
    QualityCategory,
    QualitySection,
    SummarySection,
    WarehouseSection,
    WarehouseTable,
)
from src.utils.logger import get_logger

logger = get_logger(__name__)


class DashboardService:
    """
    Builds the dashboard response from
    the pipeline execution result.
    """

    def build_dashboard(
        self,
        pipeline_result: dict,
    ) -> DashboardResponse:

        logger.info("=" * 60)
        logger.info("BUILDING DASHBOARD")
        logger.info("=" * 60)

        validation_dashboard = pipeline_result[
            "validation_dashboard"
        ]

        warehouse_summary = pipeline_result[
            "warehouse_summary"
        ]

        # ==================================================
        # KPI SECTION
        # ==================================================

        rows_processed = sum(
            len(df)
            for df in pipeline_result[
                "staging"
            ].values()
        )

        kpis = KPIModel(

            quality_score=
                validation_dashboard.quality_score,

            rows_processed=
                rows_processed,

            warehouse_tables=
                warehouse_summary.total_tables,

            execution_time=
                pipeline_result[
                    "duration_seconds"
                ],

        )

        # ==================================================
        # PIPELINE SECTION
        # ==================================================

        pipeline = PipelineStatus(

            stages=[

                PipelineStage(
                    "Landing",
                    "Completed",
                ),

                PipelineStage(
                    "Staging",
                    "Completed",
                ),

                PipelineStage(
                    "Validation",
                    "Completed",
                ),

                PipelineStage(
                    "Warehouse",
                    "Completed",
                ),

            ]

        )

        # ==================================================
        # QUALITY SECTION
        # ==================================================

        categories = []

        for (
            category_name,
            stats,
        ) in validation_dashboard.summary.categories.items():

            categories.append(

                QualityCategory(

                    name=category_name,

                    total=stats["total"],

                    passed=stats["passed"],

                    failed=stats["failed"],

                )

            )

        quality = QualitySection(

            overall_score=
                validation_dashboard.quality_score,

            categories=categories,

        )

        # ==================================================
        # WAREHOUSE SECTION
        # ==================================================

        warehouse_tables = []

        for table in warehouse_summary.tables:

            warehouse_tables.append(

                WarehouseTable(

                    name=table.table_name,

                    rows=table.rows,

                    table_type=table.table_type,

                )

            )

        warehouse = WarehouseSection(

            tables=warehouse_tables,

        )

        # ==================================================
        # SUMMARY SECTION
        # ==================================================

        summary = SummarySection(

            datasets_loaded=
                pipeline_result[
                    "summary"
                ].successful,

            validation_rules=
                validation_dashboard.summary.total_rules,

            rules_passed=
                validation_dashboard.summary.passed,

            rules_failed=
                validation_dashboard.summary.failed,

            run_timestamp=
                datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),

        )

        logger.info(
            "Dashboard model created."
        )

        # ==================================================
        # RESPONSE
        # ==================================================

        return DashboardResponse(

            status="success",

            kpis=kpis,

            pipeline=pipeline,

            quality=quality,

            warehouse=warehouse,

            summary=summary,

        )