from src.analytics.warehouse.dimensions import (
    DimensionBuilder,
)
from src.ingestion.loader import DataLoader
from src.transformation.staging import StagingEngine


def main():

    loader = DataLoader()

    datasets, _, _ = loader.run()

    staging = StagingEngine()

    staged, _ = staging.run(datasets)

    builder = DimensionBuilder()

    dimensions, results = builder.build(staged)

    print()

    print("=" * 70)
    print("DIMENSIONS")
    print("=" * 70)

    for name, df in dimensions.items():

        print(
            f"{name:<20}"
            f"{len(df):>10,} rows"
        )

    print()

    print("=" * 70)
    print("RESULTS")
    print("=" * 70)

    for result in results:

        print(result)


if __name__ == "__main__":
    main()