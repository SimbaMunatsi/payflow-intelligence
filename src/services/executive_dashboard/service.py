"""
Executive Dashboard Service.

Builds the Executive Operations Dashboard.

Author: Simba Munatsi
Project: PayFlow Intelligence Platform
"""

from src.services.executive_dashboard.charts import (
    ExecutiveChartsBuilder,
)

from src.services.executive_dashboard.metrics import (
    ExecutiveMetricsCalculator,
)

from src.services.executive_dashboard.models import (
    ExecutiveDashboard,
)

from src.utils.logger import get_logger

logger = get_logger(__name__)


class ExecutiveDashboardService:
    """
    Builds the Executive Operations Dashboard.
    """

    def __init__(self):

        self.metrics = ExecutiveMetricsCalculator()

        self.charts = ExecutiveChartsBuilder()

    # =====================================================
    # Public
    # =====================================================

    def build(
        self,
        start_date=None,
        end_date=None,
    ) -> ExecutiveDashboard:
        """
        Build the Executive Dashboard.
        """

        logger.info("=" * 60)
        logger.info(
            "BUILDING EXECUTIVE DASHBOARD"
        )
        logger.info("=" * 60)

        dashboard = ExecutiveDashboard(

            kpis=self.metrics.calculate(

                start_date=start_date,

                end_date=end_date,

            ),

            charts=self.charts.build(

                start_date=start_date,

                end_date=end_date,

            ),

        )

        logger.info(
            "Executive dashboard created successfully."
        )

        return dashboard

    def to_dict(
        self,
        start_date=None,
        end_date=None,
    ) -> dict:
        """
        Return dashboard as a serializable dictionary.
        """

        return self.build(

            start_date=start_date,

            end_date=end_date,

        ).to_dict()