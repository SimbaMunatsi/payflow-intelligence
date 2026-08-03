"""
Tests MissingRequiredValuesRule.
"""

import pandas as pd

from src.validation.structural.missing_required_values import (
    MissingRequiredValuesRule,
)


def main():

    df = pd.DataFrame(
        {
            "txn_ref": [
                "TXN001",
                "TXN002",
            ],
            "merchant_id": [
                "MER001",
                None,
            ],
            "rail": [
                "ECOCASH_MM",
                "ZIPIT_BANK",
            ],
            "currency": [
                "USD",
                "USD",
            ],
            "amount": [
                120,
                None,
            ],
            "status": [
                "SUCCESS",
                "SUCCESS",
            ],
            "initiated_at": [
                "2026-03-01",
                None,
            ],
        }
    )

    rule = MissingRequiredValuesRule(
        "transactions"
    )

    result = rule.execute(df)

    print(result)

    print()

    print(result.to_dict())


if __name__ == "__main__":
    main()