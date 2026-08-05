"""
Test Executive KPI Calculator.

Author: Simba Munatsi
Project: PayFlow Intelligence Platform
"""

from src.services.executive_dashboard.metrics import (
    ExecutiveMetricsCalculator,
)


def main():

    calculator = ExecutiveMetricsCalculator()

    kpis = calculator.calculate()

    print("\n" + "=" * 60)
    print("EXECUTIVE KPI TEST")
    print("=" * 60)

    print(f"Total Transactions      : {kpis.total_transactions:,}")
    print(f"Success Rate            : {kpis.success_rate:.2f}%")
    print(f"Settlement Rate         : {kpis.settlement_rate:.2f}%")
    print(f"Total Volume (USD)      : {kpis.total_volume_usd:,.2f}")
    print(f"Total Volume (ZWG)      : {kpis.total_volume_zwg:,.2f}")
    print(f"Average Settlement Lag  : {kpis.average_settlement_lag:.2f} days")
    print(f"Open Support Tickets    : {kpis.open_support_tickets:,}")

    print("=" * 60)
    print("TEST PASSED")
    print("=" * 60)


if __name__ == "__main__":

    main()