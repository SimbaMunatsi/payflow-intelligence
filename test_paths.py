"""
Tests the Staging Engine.

Author: Simba Munatsi
"""

from src.ingestion.loader import DataLoader
from src.transformation.staging import (
    StagingEngine,
)


def main():

    loader = DataLoader()

    datasets, metadata, summary = loader.run()

    staging = StagingEngine()

    staged_datasets, results = staging.run(
        datasets,
    )

    print("\n")

    print("=" * 70)
    print("STAGING DATASETS")
    print("=" * 70)

    for name, df in staged_datasets.items():

        print(f"{name:15} {len(df):>10,} rows")

    print("\n")

    print("=" * 70)
    print("TRANSFORMATION RESULTS")
    print("=" * 70)

    for result in results:

        print(result.to_dict())


if __name__ == "__main__":
    main()