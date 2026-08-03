"""
Validation Dashboard Builder.

Builds the dashboard model consumed by the
Pipeline Control Center, APIs and Streamlit UI.

Author: Simba Munatsi
Project: PayFlow Intelligence Platform
"""

from src.validation.analytics.models import (
    DashboardModel,
)

from src.validation.analytics.score import (
    QualityScoreCalculator,
)

from src.validation.analytics.summary import (
    ValidationSummaryBuilder,
)

from src.validation.framework.results import (
    ValidationResult,
)


class ValidationDashboardBuilder:
    """
    Builds dashboard-ready validation analytics.
    """

    def __init__(self):

        self.summary_builder = ValidationSummaryBuilder()

        self.score_calculator = QualityScoreCalculator()

    def build(
        self,
        results: list[ValidationResult],
    ) -> DashboardModel:

        summary = self.summary_builder.build(
            results
        )

        score = self.score_calculator.calculate(
            results
        )

        return DashboardModel(

            quality_score=score,

            summary=summary,

        )