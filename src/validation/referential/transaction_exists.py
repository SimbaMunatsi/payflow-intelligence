"""
Transaction Exists Validation Rule.

Ensures that every referenced transaction exists
in the transactions dataset.

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


class TransactionExistsRule(ValidationRule):
    """
    Validates transaction referential integrity.
    """

    @property
    def rule_name(self):
        return "Transaction Exists"

    @property
    def severity(self):
        return "CRITICAL"

    @property
    def category(self):
        return "Referential"

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

        if "txn_ref" not in foreign_keys:

            return ValidationResult(
                rule_name=self.rule_name,
                dataset=self.dataset_name,
                category=self.category,
                passed=True,
                severity="INFO",
                message="Dataset has no transaction relationship.",
            )

        if datasets is None or "transactions" not in datasets:

            return ValidationResult(
                rule_name=self.rule_name,
                dataset=self.dataset_name,
                category=self.category,
                passed=False,
                severity="CRITICAL",
                message="Transactions dataset not available.",
                recommendation="Load transactions before referential validation.",
            )

        relationship = foreign_keys["txn_ref"]

        nullable = relationship.get(
            "nullable",
            False,
        )

        transactions = datasets["transactions"]

        valid_txns = set(
            transactions["txn_ref"]
            .dropna()
            .astype(str)
        )

        if nullable:

            references = (
                dataframe["txn_ref"]
                .dropna()
                .astype(str)
            )

        else:

            references = (
                dataframe["txn_ref"]
                .astype(str)
            )

        invalid_txns = sorted(
            set(references)
            - valid_txns
        )

        passed = len(invalid_txns) == 0

        return ValidationResult(

            rule_name=self.rule_name,

            dataset=self.dataset_name,

            category=self.category,

            passed=passed,

            severity=self.severity,

            message=(
                "All transaction references exist."
                if passed
                else (
                    f"{len(invalid_txns)} invalid transaction reference(s) found."
                )
            ),

            rows_affected=len(invalid_txns),

            recommendation=(
                ""
                if passed
                else "Investigate orphan switch logs or support tickets."
            ),

            details={
                "invalid_transactions": invalid_txns,
            },
        )