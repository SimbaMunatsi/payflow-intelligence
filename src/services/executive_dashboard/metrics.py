"""
Executive KPI Calculator.

Computes executive business KPIs from the
analytics warehouse.

Author: Simba Munatsi
Project: PayFlow Intelligence Platform
"""

from src.services.filters.date_filter import (
    DateFilter,
)
import pandas as pd

from src.services.executive_dashboard.models import (
    ExecutiveKPIs,
)

from src.utils.logger import get_logger
from src.utils.paths import WAREHOUSE_DATA_DIR

logger = get_logger(__name__)


class ExecutiveMetricsCalculator:
    """
    Calculates executive business KPIs.
    """

    def __init__(self):

        self.transactions = pd.read_parquet(
            WAREHOUSE_DATA_DIR
            / "fact_transactions.parquet"
        )

        self.settlements = pd.read_parquet(
            WAREHOUSE_DATA_DIR
            / "fact_settlements.parquet"
        )

        self.tickets = pd.read_parquet(
            WAREHOUSE_DATA_DIR
            / "fact_support_tickets.parquet"
        )

    # =====================================================
    # Public
    # =====================================================

    def calculate(
        self,
        start_date=None,
        end_date=None,
    ) -> ExecutiveKPIs:
        """
        Calculate executive KPIs for the
        selected date range.
        """

        logger.info(
            "Calculating executive KPIs."
        )

        transactions = DateFilter.filter(

            self.transactions,

            date_column="initiated_at",

            start_date=start_date,

            end_date=end_date,

        )

        settlements = DateFilter.filter(

            self.settlements,

            date_column="value_date",

            start_date=start_date,

            end_date=end_date,

        )

        return ExecutiveKPIs(

            total_transactions=
                self.total_transactions(
                    transactions
                ),

            success_rate=
                self.success_rate(
                    transactions
                ),

            settlement_rate=
                self.settlement_rate(
                    transactions,
                    settlements,
                ),

            total_volume_usd=
                self.total_volume_usd(
                    transactions
                ),

            total_volume_zwg=
                self.total_volume_zwg(
                    transactions
                ),

            average_settlement_lag=
                self.average_settlement_lag(
                    transactions,
                    settlements,
                ),

            open_support_tickets=
                self.open_support_tickets(),

        )

    # =====================================================
    # Individual KPIs
    # =====================================================

    def total_transactions(self, transactions) -> int:

        return len(
            transactions
        )

    def success_rate(self, transactions) -> float:

        if len(transactions) == 0:

            return 0.0

        successful = (

            transactions["status"]

            .astype(str)

            .str.upper()

            .eq("SUCCESS")

            .sum()

        )

        return (

            successful

            / len(transactions)

            * 100

        )

    def settlement_rate(self, transactions, settlements) -> float:

        if len(transactions) == 0:

            return 0.0

        settled = len(
            settlements
        )

        return (

            settled

            / len(transactions)

            * 100

        )

    def total_volume_usd(self, transactions) -> float:

        usd = transactions[
            transactions["currency"]
            .astype(str)
            .str.upper()
            == "USD"
        ]

        return float(

            usd["amount"].sum()

        )

    def total_volume_zwg(self, transactions) -> float:

        zwg = transactions[
            transactions["currency"]
            .astype(str)
            .str.upper()
            == "ZWG"
        ]

        return float(

            zwg["amount"].sum()

        )

    def average_settlement_lag(self, transactions, settlements) -> float:
        """
        Average days between transaction initiation
        and settlement value date.
        """

        merged = transactions.merge(

            settlements[

                [

                    "rail_reference",

                    "value_date",

                ]

            ],

            left_on="txn_ref",

            right_on="rail_reference",

            how="inner",

        )

        if merged.empty:

            return 0.0

        lag = (

            merged["value_date"]

            - merged["initiated_at"]

        ).dt.days

        return float(

            lag.mean()

        )

    def open_support_tickets(self) -> int:
        """
        Count tickets that are still awaiting resolution.
        """

        active_statuses = [

            "OPEN",

            "PENDING_MERCHANT",

        ]

        return int(

            self.tickets["status"]

            .astype(str)

            .str.upper()

            .isin(active_statuses)

            .sum()

        )