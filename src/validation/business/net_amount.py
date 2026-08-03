"""
Net Amount Validation Rule.

Validates that:

net_amount = gross_amount - rail_charges

Author: Simba Munatsi
Project: PayFlow Intelligence Platform
"""

import numpy as np
import pandas as pd

from src.validation.framework.results import (
    ValidationResult,
)

from src.validation.framework.rules import (
    ValidationRule,
)


class NetAmountRule(ValidationRule):

    @property
    def rule_name(self):
        return "Net Amount Validation"

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

        expected = (
            dataframe["gross_amount"]
            - dataframe["rail_charges"]
        )

        valid = np.isclose(
            expected,
            dataframe["net_amount"],
            atol=0.01,
            equal_nan=True,
        )

        invalid_rows = dataframe.loc[
            ~valid
        ]

        passed = len(invalid_rows) == 0

        return ValidationResult(

            rule_name=self.rule_name,

            dataset=self.dataset_name,

            passed=passed,

            severity=self.severity,

            message=(
                "Net amount calculation is correct."
                if passed
                else f"{len(invalid_rows)} invalid net amount calculation(s)."
            ),

            rows_affected=len(invalid_rows),

            recommendation=(
                ""
                if passed
                else "Verify settlement calculations before publishing settlement batches."
            ),

            details={
                "invalid_rows": invalid_rows.index.tolist(),
            },

        )