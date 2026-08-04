"""
Pipeline Service.

Responsible only for executing the PayFlow
Intelligence pipeline.

Author: Simba Munatsi
Project: PayFlow Intelligence Platform
"""

from src.pipeline.orchestrator import PipelineOrchestrator
from src.utils.logger import get_logger

logger = get_logger(__name__)


class PipelineService:
    """
    Executes the pipeline.
    """

    def __init__(self):

        self.pipeline = PipelineOrchestrator()

    def run_pipeline(self):
        """
        Execute the pipeline and return the
        complete orchestration result.
        """

        logger.info("=" * 60)
        logger.info("PIPELINE SERVICE")
        logger.info("=" * 60)

        result = self.pipeline.run()

        logger.info(
            "Pipeline execution completed."
        )

        return result