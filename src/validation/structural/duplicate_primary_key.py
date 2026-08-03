"""
Duplicate Primary Key Validation Rule.

Ensures that the business primary key for each dataset
contains unique values.

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


class DuplicatePrimaryKeyRule(ValidationRule):
    """
    Validates uniqueness of business primary keys.
    """

    @property
    def rule_name(self):
        return "Duplicate Primary Keys"

    @property
    def severity(self):
        return "CRITICAL"

    def validate(
        self,
        dataframe: pd.DataFrame,
        datasets=None,
    ):

        metadata = METADATA_REGISTRY.get(
            self.dataset_name,
            {},
        )

        primary_key = metadata.get(
            "primary_key",
            [],
        )

        if not primary_key:

            return ValidationResult(
                rule_name=self.rule_name,
                dataset=self.dataset_name,
                passed=True,
                severity="INFO",
                message="No primary key defined.",
                recommendation="",
            )

        duplicate_mask = dataframe.duplicated(
            subset=primary_key,
            keep=False,
        )

        duplicate_rows = dataframe.loc[
            duplicate_mask,
            primary_key,
        ]

        passed = duplicate_rows.empty

        return ValidationResult(

            rule_name=self.rule_name,

            dataset=self.dataset_name,

            passed=passed,

            severity=self.severity,

            message=(
                "Primary key is unique."
                if passed
                else f"{len(duplicate_rows)} duplicate primary key row(s) found."
            ),

            rows_affected=len(duplicate_rows),

            recommendation=(
                ""
                if passed
                else "Investigate duplicate records before loading into the warehouse."
            ),

            details={
                "primary_key": primary_key,
                "duplicate_keys": duplicate_rows.to_dict(
                    orient="records"
                ),
            },
        )