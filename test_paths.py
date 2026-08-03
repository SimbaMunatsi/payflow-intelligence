"""
Tests RequiredColumnsRule.

Author: Simba Munatsi
"""

import pandas as pd

from src.validation.structural.required_columns import (
    RequiredColumnsRule,
)


def main():

    df = pd.DataFrame(
        {
            "txn_ref": ["TXN001"],
           # "merchant_id": ["MER001"],
            "amount": [100],
            "currency": ["USD"],
            "rail": ["ECOCASH_MM"],
            "status": ["SUCCESS"],
            "initiated_at": ["2026-03-01"],
        }
    )

    rule = RequiredColumnsRule(
        "transactions"
    )

    result = rule.execute(df)

    print(result)

    print()

    print(result.to_dict())


if __name__ == "__main__":
    main()