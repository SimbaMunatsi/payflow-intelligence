"""
Data Quality Score Calculator.

Calculates an overall quality score from validation
results.

Author: Simba Munatsi
Project: PayFlow Intelligence Platform
"""

from src.validation.framework.results import ValidationResult


PENALTIES = {

    "CRITICAL": 5,

    "ERROR": 3,

    "WARNING": 1,

    "INFO": 0,

}


class QualityScoreCalculator:

    """
    Calculates an overall data quality score.
    """

    STARTING_SCORE = 100

    def calculate(
        self,
        results: list[ValidationResult],
    ) -> float:

        score = self.STARTING_SCORE

        for result in results:

            if result.passed:
                continue

            score -= PENALTIES.get(
                result.severity,
                0,
            )

        return max(
            round(score, 2),
            0,
        )