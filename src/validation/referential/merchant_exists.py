"""
Merchant Exists Validation Rule.

Ensures that every merchant referenced in a dataset
exists in the merchants master dataset.

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


class MerchantExistsRule(ValidationRule):
    """
    Validates merchant referential integrity.
    """

    @property
    def rule_name(self):
        return "Merchant Exists"

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

        foreign_keys = metadata.get(
            "foreign_keys",
            {},
        )

        # Does this dataset even reference merchants?
        if "merchant_id" not in foreign_keys:

            return ValidationResult(
                rule_name=self.rule_name,
                dataset=self.dataset_name,
                passed=True,
                severity="INFO",
                message="Dataset has no merchant relationship.",
            )

        if datasets is None or "merchants" not in datasets:

            return ValidationResult(
                rule_name=self.rule_name,
                dataset=self.dataset_name,
                passed=False,
                severity="CRITICAL",
                message="Merchants dataset not available.",
                recommendation="Load merchants dataset before running referential validation.",
            )

        merchants = datasets["merchants"]

        valid_merchants = set(
            merchants["merchant_id"]
            .dropna()
            .astype(str)
        )

        transaction_merchants = (
            dataframe["merchant_id"]
            .dropna()
            .astype(str)
        )

        invalid_merchants = sorted(
            set(transaction_merchants)
            - valid_merchants
        )

        passed = len(invalid_merchants) == 0

        return ValidationResult(

            rule_name=self.rule_name,

            dataset=self.dataset_name,

            passed=passed,

            severity=self.severity,

            message=(
                "All merchants exist."
                if passed
                else (
                    f"{len(invalid_merchants)} unknown merchant(s) found."
                )
            ),

            rows_affected=len(invalid_merchants),

            recommendation=(
                ""
                if passed
                else "Verify merchant onboarding or investigate orphan transactions."
            ),

            details={
                "missing_merchants": invalid_merchants,
            },
        )