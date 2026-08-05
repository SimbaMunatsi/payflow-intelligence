"""
Test Executive Dashboard Service.
"""

from src.services.executive_dashboard.service import (
    ExecutiveDashboardService,
)


def main():

    service = ExecutiveDashboardService()

    dashboard = service.build()

    print("\n" + "=" * 60)
    print("EXECUTIVE DASHBOARD TEST")
    print("=" * 60)

    print()

    print(dashboard.kpis)

    print()

    print(f"Charts: {len(dashboard.charts)}")

    for chart in dashboard.charts:

        print(f"✓ {chart.title}")

    print()

    print("=" * 60)
    print("TEST PASSED")
    print("=" * 60)


if __name__ == "__main__":

    main()