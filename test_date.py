"""
Test Executive Charts.

Author: Simba Munatsi
Project: PayFlow Intelligence Platform
"""

from src.services.executive_dashboard.charts import (
    ExecutiveChartsBuilder,
)


def main():

    builder = ExecutiveChartsBuilder()

    charts = builder.build(

        start_date="2026-03-10",

        end_date="2026-03-20",

    )

    print("\n" + "=" * 60)
    print("EXECUTIVE CHART TEST")
    print("=" * 60)

    print(f"\nCharts Generated: {len(charts)}\n")

    for chart in charts:

        print(f"✓ {chart.title}")
        print(f"  Type   : {chart.chart_type}")
        print(f"  Labels : {len(chart.labels)}")
        print(f"  Values : {len(chart.values)}")
        print("-" * 60)

    print("\nTEST PASSED")
    print("=" * 60)


if __name__ == "__main__":

    main()