"""
Tests MerchantExistsRule.
"""

import pandas as pd

from src.validation.referential.merchant_exists import (
    MerchantExistsRule,
)


def main():

    merchants = pd.DataFrame(
        {
            "merchant_id": [
                "MER001",
                "MER002",
            ]
        }
    )

    transactions = pd.DataFrame(
        {
            "merchant_id": [
                "MER001",
                "MER999",
                "MER002",
            ]
        }
    )

    datasets = {
        "merchants": merchants,
        "transactions": transactions,
    }

    rule = MerchantExistsRule(
        "transactions"
    )

    result = rule.execute(
        transactions,
        datasets,
    )

    print(result)
    print()
    print(result.to_dict())


if __name__ == "__main__":
    main()