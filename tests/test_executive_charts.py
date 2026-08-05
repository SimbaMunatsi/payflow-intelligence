from src.services.executive_dashboard.charts import (
    ExecutiveChartsBuilder,
)


builder = ExecutiveChartsBuilder()

charts = builder.build()

print("=" * 60)

print("EXECUTIVE CHART TEST")

print("=" * 60)

for chart in charts:

    print()

    print(chart.title)

    print(chart.chart_type)

    print(chart.labels)

    print(chart.values)

print()

print("TEST PASSED")