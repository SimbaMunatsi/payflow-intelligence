from src.pipeline.orchestrator import (
    PipelineOrchestrator,
)


def main():

    pipeline = PipelineOrchestrator()

    result = pipeline.run()

    print()

    print("=" * 70)
    print("PAYFLOW INTELLIGENCE PLATFORM")
    print("=" * 70)

    print()

    dashboard = result["validation_dashboard"]

    print(
        f"Data Quality Score : "
        f"{dashboard.quality_score}"
    )

    warehouse = result["warehouse_summary"]

    print(
        f"Warehouse Tables : "
        f"{warehouse.total_tables}"
    )

    print(
        f"Warehouse Success : "
        f"{warehouse.success_rate}%"
    )

    print()

    print("=" * 70)
    print("WAREHOUSE")
    print("=" * 70)

    for table in warehouse.tables:

        print(

            f"{table.table_name:<30}"

            f"{table.rows:>12,}"

        )


if __name__ == "__main__":
    main()