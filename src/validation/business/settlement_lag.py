"""
Settlement Lag Validation Rule.

Validates that settlement value dates follow the
published settlement lag for each payment rail.

Author: Simba Munatsi
Project: PayFlow Intelligence Platform
"""

import pandas as pd
from pandas.tseries.offsets import BusinessDay

from src.transformation.metadata_registry import PAYMENT_RAILS
from src.validation.framework.results import ValidationResult
from src.validation.framework.rules import ValidationRule


class SettlementLagRule(ValidationRule):

    @property
    def rule_name(self):
        return "Settlement Lag Validation"

    @property
    def severity(self):
        return "CRITICAL"

    def validate(
        self,
        dataframe: pd.DataFrame,
        datasets=None,
    ):

        if self.dataset_name != "settlements":

            return ValidationResult(
                rule_name=self.rule_name,
                dataset=self.dataset_name,
                passed=True,
                severity="INFO",
                message="Rule not applicable.",
            )

        if datasets is None:

            return ValidationResult(
                rule_name=self.rule_name,
                dataset=self.dataset_name,
                passed=False,
                severity="CRITICAL",
                message="Datasets unavailable.",
            )

        if "transactions" not in datasets:

            return ValidationResult(
                rule_name=self.rule_name,
                dataset=self.dataset_name,
                passed=False,
                severity="CRITICAL",
                message="Transactions dataset unavailable.",
            )

        if "switch_log" not in datasets:

            return ValidationResult(
                rule_name=self.rule_name,
                dataset=self.dataset_name,
                passed=False,
                severity="CRITICAL",
                message="Switch Log dataset unavailable.",
            )

        transactions = datasets["transactions"]

        switch_log = datasets["switch_log"]

        # ----------------------------------------------------
        # Join Transactions -> Switch Log
        # ----------------------------------------------------

        transaction_switch = switch_log.merge(

            transactions[
                [
                    "txn_ref",
                    "authorised_at",
                ]
            ],

            on="txn_ref",

            how="left",

        )

        # ----------------------------------------------------
        # Join -> Settlements
        # ----------------------------------------------------

        merged = dataframe.merge(

            transaction_switch[
                [
                    "rail_reference",
                    "authorised_at",
                ]
            ],

            on="rail_reference",

            how="left",

        )

        merged["authorised_at"] = pd.to_datetime(
            merged["authorised_at"]
        )

        merged["value_date"] = pd.to_datetime(
            merged["value_date"]
        )

        # ----------------------------------------------------
        # Expected Settlement Date
        # ----------------------------------------------------

        def calculate_expected_date(row):

            metadata = PAYMENT_RAILS.get(
                row["rail"]
            )

            if metadata is None:
                return pd.NaT

            if pd.isna(row["authorised_at"]):
                return pd.NaT

            lag = metadata["settlement_lag_days"]

            return (
                row["authorised_at"]
                + BusinessDay(lag)
            )

        merged["expected_value_date"] = merged.apply(

            calculate_expected_date,

            axis=1,

        )

        valid = (

            merged["value_date"].dt.normalize()

            ==

            merged["expected_value_date"].dt.normalize()

        )

        invalid_rows = merged.loc[
            ~valid
        ]

        passed = invalid_rows.empty

        return ValidationResult(

            rule_name=self.rule_name,

            dataset=self.dataset_name,

            passed=passed,

            severity=self.severity,

            message=(

                "Settlement lag is correct."

                if passed

                else f"{len(invalid_rows)} settlement lag issue(s) found."

            ),

            rows_affected=len(invalid_rows),

            recommendation=(

                ""

                if passed

                else "Investigate delayed or early settlements."

            ),

            details={

                "invalid_rows": invalid_rows[
                    [
                        "rail",
                        "rail_reference",
                        "authorised_at",
                        "value_date",
                        "expected_value_date",
                    ]
                ].to_dict(
                    orient="records"
                )

            },

        )