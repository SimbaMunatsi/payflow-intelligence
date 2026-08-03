"""
Runs the complete PayFlow Intelligence pipeline.

Author: Simba Munatsi
"""

from src.pipeline.orchestrator import (
    PipelineOrchestrator,
)


def main():

    pipeline = PipelineOrchestrator()

    result = pipeline.run()

    dashboard = result["validation_dashboard"]

    print()

    print("=" * 70)
    print("PIPELINE COMPLETE")
    print("=" * 70)

    print()

    print(
        f"Quality Score : {dashboard.quality_score}"
    )

    print()

    print(
        f"Rules Checked : {dashboard.summary.total_rules}"
    )

    print(
        f"Passed        : {dashboard.summary.passed}"
    )

    print(
        f"Failed        : {dashboard.summary.failed}"
    )

    print()

    print("=" * 70)
    print("DATASETS")
    print("=" * 70)

    for dataset in dashboard.summary.datasets.values():

        print(dataset)

    print()

    print("=" * 70)
    print("CATEGORIES")
    print("=" * 70)

    for category, values in (
        dashboard.summary.categories.items()
    ):

        print(category)

        print(values)

        print()


if __name__ == "__main__":
    main()