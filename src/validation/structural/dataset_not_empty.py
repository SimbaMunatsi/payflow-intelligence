"""
Sample validation rule.

Author: Simba Munatsi
"""

from src.validation.framework.results import ValidationResult
from src.validation.framework.rules import ValidationRule


class DatasetNotEmptyRule(ValidationRule):

    @property
    def rule_name(self):

        return "Dataset Not Empty"

    @property
    def category(self):
        return "Structural"

    def validate(
        self,
        dataframe,
        datasets=None,
    ):

        passed = len(dataframe) > 0

        return ValidationResult(

            rule_name=self.rule_name,

            dataset=self.dataset_name,

            category=self.category,

            passed=passed,

            severity=self.severity,

            message=(
                "Dataset contains records."
                if passed
                else "Dataset is empty."
            ),

            rows_affected=0 if passed else 1,

            recommendation=(
                ""
                if passed
                else "Verify source export."
            ),
        )