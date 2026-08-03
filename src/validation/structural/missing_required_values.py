"""
Missing Required Values Validation Rule.

Ensures that required columns contain values.

Author: Simba Munatsi
Project: PayFlow Intelligence Platform
"""

import pandas as pd

from src.transformation.metadata_registry import (
    METADATA_REGISTRY,
)

from src.validation.framework.results import (
    ValidationResult,
)

from src.validation.framework.rules import (
    ValidationRule,
)


class MissingRequiredValuesRule(ValidationRule):
    """
    Validates that required columns do not contain
    missing values.
    """

    @property
    def rule_name(self):
        return "Missing Required Values"

    @property
    def severity(self):
        return "ERROR"

    @property
    def category(self):
        return "Structural"

    def validate(
        self,
        dataframe: pd.DataFrame,
        datasets=None,
    ):

        metadata = METADATA_REGISTRY.get(
            self.dataset_name,
            {},
        )

        required_columns = metadata.get(
            "required",
            [],
        )

        missing_summary = {}

        total_missing = 0

        for column in required_columns:

            if column not in dataframe.columns:
                continue

            missing = dataframe[column].isna().sum()

            if missing > 0:

                missing_summary[column] = int(missing)

                total_missing += int(missing)

        passed = total_missing == 0

        return ValidationResult(

            rule_name=self.rule_name,

            dataset=self.dataset_name,

            category="Structural",

            passed=passed,

            severity=self.severity,

            message=(
                "All required fields contain values."
                if passed
                else f"{total_missing} missing required value(s) found."
            ),

            rows_affected=total_missing,

            recommendation=(
                ""
                if passed
                else "Populate missing mandatory fields before loading into the warehouse."
            ),

            details={
                "missing_values_by_column": missing_summary,
            },
        )