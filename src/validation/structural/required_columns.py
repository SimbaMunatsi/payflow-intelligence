"""
Required Columns Validation Rule.

Ensures that all required columns defined in the
Metadata Registry exist in the dataset.

Author: Simba Munatsi
Project: PayFlow Intelligence Platform
"""

from src.transformation.metadata_registry import (
    METADATA_REGISTRY,
)

from src.validation.framework.results import (
    ValidationResult,
)

from src.validation.framework.rules import (
    ValidationRule,
)


class RequiredColumnsRule(ValidationRule):
    """
    Validate that required columns exist.
    """

    @property
    def rule_name(self):

        return "Required Columns"

    @property
    def severity(self):

        return "CRITICAL"

    @property
    def category(self):
        return "Structural"

    def validate(
        self,
        dataframe,
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

        missing_columns = [

            column

            for column in required_columns

            if column not in dataframe.columns

        ]

        passed = len(missing_columns) == 0

        return ValidationResult(

            rule_name=self.rule_name,

            dataset=self.dataset_name,

            category="Structural",

            passed=passed,

            severity=self.severity,

            message=(

                "All required columns exist."

                if passed

                else f"Missing required columns: {', '.join(missing_columns)}"

            ),

            rows_affected=len(missing_columns),

            recommendation=(

                ""

                if passed

                else "Verify the source system export or update the ingestion mapping."

            ),

            details={

                "required_columns": required_columns,

                "missing_columns": missing_columns,

            },

        )