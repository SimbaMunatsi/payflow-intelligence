"""
Tests DuplicatePrimaryKeyRule.
"""

import pandas as pd

from src.validation.structural.duplicate_primary_key import (
    DuplicatePrimaryKeyRule,
)


def main():

    df = pd.DataFrame(
        {
            "txn_ref": [
                "TXN001",
                "TXN002",
                "TXN001",
            ],
            "merchant_id": [
                "MER001",
                "MER002",
                "MER003",
            ],
            "amount": [
                100,
                200,
                150,
            ],
        }
    )

    rule = DuplicatePrimaryKeyRule(
        "transactions"
    )

    result = rule.execute(df)

    print(result)

    print()

    print(result.to_dict())


if __name__ == "__main__":
    main()