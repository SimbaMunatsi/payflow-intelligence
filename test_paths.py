"""
Tests the DataCleaner transformation engine.

Author: Simba Munatsi
Project: PayFlow Intelligence Platform
"""

import pandas as pd

from src.transformation.cleaning import DataCleaner


def main():

    # Sample dirty data
    df = pd.DataFrame(
        {
            "merchant": [
                " MER001 ",
                "MER002 ",
                "",
            ],
            "status": [
                " SUCCESS ",
                "FAILED ",
                " NULL ",
            ],
            "amount": [
                "100.50",
                "250.00",
                "",
            ],
        }
    )

    cleaner = DataCleaner()

    cleaned_df, results = cleaner.clean(
        dataset_name="transactions",
        dataframe=df,
    )

    print("=" * 70)
    print("CLEANED DATAFRAME")
    print("=" * 70)
    print(cleaned_df)

    print("\n")

    print("=" * 70)
    print("DATA TYPES")
    print("=" * 70)
    print(cleaned_df.dtypes)

    print("\n")

    print("=" * 70)
    print("TRANSFORMATION RESULTS")
    print("=" * 70)

    for result in results:
        print(result.to_dict())


if __name__ == "__main__":
    main()