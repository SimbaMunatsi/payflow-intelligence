"""
Pipeline Service.

Executes the PayFlow Intelligence pipeline and
returns a simplified response for the API.

Author: Simba Munatsi
Project: PayFlow Intelligence Platform
"""

from datetime import datetime
from src.pipeline.orchestrator import PipelineOrchestrator
from src.utils.logger import get_logger


logger = get_logger(__name__)


class PipelineService:
    """
    Service responsible for executing the pipeline.
    """

    def __init__(self):

        self.pipeline = PipelineOrchestrator()

    def run_pipeline(self):

        logger.info("=" * 60)
        logger.info("PIPELINE SERVICE")
        logger.info("=" * 60)

        result = self.pipeline.run()

        dashboard = result["validation_dashboard"]

        warehouse = result["warehouse_summary"]
        
        response = {

            "status": "success",

            "duration_seconds":
                result["duration_seconds"],

            "quality_score":
                dashboard.quality_score
                if dashboard else 0,

            "warehouse_tables":
                warehouse.total_tables
                if warehouse else 0,

            "warehouse_success_rate":
                warehouse.success_rate
                if warehouse else 0,

            "datasets_loaded":
                result["summary"].successful
                if result["summary"] else 0,

            "validation_rules":
                dashboard.summary.total_rules
                if dashboard else 0,

            "rules_passed":
                dashboard.summary.passed
                if dashboard else 0,

            "rules_failed":
                dashboard.summary.failed
                if dashboard else 0,

            "rows_processed":
                sum(
                    len(df)
                    for df in result["staging"].values()
                ),

            "run_timestamp":
                datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),

            "stages": {

                "landing": "Completed",

                "staging": "Completed",

                "validation": "Completed",

                "warehouse": "Completed",

            },

        }

        logger.info(
            "Pipeline execution completed."
        )

        return response