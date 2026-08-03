"""
Rail Charges Validation Rule.

Validates that rail charges match the published
payment rail charge rates.

Author: Simba Munatsi
Project: PayFlow Intelligence Platform
"""

import numpy as np
import pandas as pd

from src.transformation.metadata_registry import (
    PAYMENT_RAILS,
)

from src.validation.framework.results import (
    ValidationResult,
)

from src.validation.framework.rules import (
    ValidationRule,
)


class RailChargesRule(ValidationRule):
    """
    Validate rail charges against published rates.
    """

    @property
    def rule_name(self):
        return "Rail Charges Validation"

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

        df = dataframe.copy()

        # ---------------------------------------------------
        # Calculate expected charges
        # ---------------------------------------------------

        df["expected_charge"] = df.apply(
            self._calculate_expected_charge,
            axis=1,
        )

        valid = np.isclose(
            df["expected_charge"],
            df["rail_charges"],
            atol=0.01,
            equal_nan=True,
        )

        invalid_rows = df.loc[~valid]

        passed = invalid_rows.empty

        return ValidationResult(

            rule_name=self.rule_name,

            dataset=self.dataset_name,

            passed=passed,

            severity=self.severity,

            message=(
                "Rail charges are correct."
                if passed
                else f"{len(invalid_rows)} incorrect rail charge(s) found."
            ),

            rows_affected=len(invalid_rows),

            recommendation=(
                ""
                if passed
                else (
                    "Verify settlement charge calculations "
                    "against published rail pricing."
                )
            ),

            details={
                "invalid_rows": invalid_rows[
                    [
                        "rail",
                        "gross_amount",
                        "rail_charges",
                        "expected_charge",
                    ]
                ].to_dict(
                    orient="records"
                )
            },

        )

    def _calculate_expected_charge(
        self,
        row,
    ) -> float:

        rail = row["rail"]

        gross = row["gross_amount"]

        metadata = PAYMENT_RAILS.get(
            rail,
        )

        if metadata is None:

            return np.nan

        rate = metadata["charge_rate"]

        return round(
            gross * rate,
            2,
        )