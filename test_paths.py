"""
Tests the DataStandardizer.

Author: Simba Munatsi
Project: PayFlow Intelligence Platform
"""

import pandas as pd

from src.transformation.standardization import (
    DataStandardizer,
)


def main():

    df = pd.DataFrame(
        {
            "currency": [
                "usd",
                "zwg",
            ],
            "status": [
                "success",
                "failed",
            ],
            "amount": [
                "100.50",
                "250",
            ],
            "attempt_count": [
                "1",
                "2",
            ],
            "initiated_at": [
                "2026-03-01 08:00:00",
                "2026-03-02 10:15:00",
            ],
        }
    )

    standardizer = DataStandardizer()

    standardized_df, results = standardizer.standardize(
        "transactions",
        df,
    )

    print("=" * 70)
    print("STANDARDIZED DATAFRAME")
    print("=" * 70)
    print(standardized_df)

    print("\n")

    print("=" * 70)
    print("DATA TYPES")
    print("=" * 70)
    print(standardized_df.dtypes)

    print("\n")

    print("=" * 70)
    print("TRANSFORMATION RESULTS")
    print("=" * 70)

    for result in results:
        print(result.to_dict())


if __name__ == "__main__":
    main()