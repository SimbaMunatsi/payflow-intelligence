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

    @property
    def category(self):
        return "Business"

    def validate(
        self,
        dataframe: pd.DataFrame,
        datasets=None,
    ):

        if self.dataset_name != "settlements":

            return ValidationResult(
                rule_name=self.rule_name,
                dataset=self.dataset_name,
                category=self.category,
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

        comparison_mask = (
            df["gross_amount"].notna()
            &
            df["rail_charges"].notna()
        )

        valid = np.ones(
            len(df),
            dtype=bool,
        )

        valid[comparison_mask] = np.isclose(

            df.loc[
                comparison_mask,
                "expected_charge",
            ],

            df.loc[
                comparison_mask,
                "rail_charges",
            ],

            atol=0.01,

        )

        invalid_rows = df.loc[~valid]

        passed = invalid_rows.empty

        return ValidationResult(

            rule_name=self.rule_name,

            dataset=self.dataset_name,

            category=self.category,

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
    ):
        """
        Calculate the expected rail charge.

        Returns NaN when the calculation
        cannot be performed.
        """

        rail = row["rail"]

        gross = row["gross_amount"]

        # ------------------------------------
        # Missing values
        # ------------------------------------

        if pd.isna(gross):

            return float("nan")

        metadata = PAYMENT_RAILS.get(
            rail
        )

        if metadata is None:

            return float("nan")

        rate = metadata["charge_rate"]

        return round(
            float(gross) * rate,
            2,
        )