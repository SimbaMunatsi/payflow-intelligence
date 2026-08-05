"""
Executive KPI Calculator.

Computes executive business KPIs from the
analytics warehouse.

Author: Simba Munatsi
Project: PayFlow Intelligence Platform
"""

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

    def calculate(self) -> ExecutiveKPIs:
        """
        Calculate all executive KPIs.
        """

        logger.info(
            "Calculating executive KPIs."
        )

        return ExecutiveKPIs(

            total_transactions=self.total_transactions(),

            success_rate=self.success_rate(),

            settlement_rate=self.settlement_rate(),

            total_volume_usd=self.total_volume_usd(),

            total_volume_zwg=self.total_volume_zwg(),

            average_settlement_lag=self.average_settlement_lag(),

            open_support_tickets=self.open_support_tickets(),

        )

    # =====================================================
    # Individual KPIs
    # =====================================================

    def total_transactions(self) -> int:

        return len(
            self.transactions
        )

    def success_rate(self) -> float:

        if len(self.transactions) == 0:

            return 0.0

        successful = (

            self.transactions["status"]

            .astype(str)

            .str.upper()

            .eq("SUCCESS")

            .sum()

        )

        return (

            successful

            / len(self.transactions)

            * 100

        )

    def settlement_rate(self) -> float:

        if len(self.transactions) == 0:

            return 0.0

        settled = len(
            self.settlements
        )

        return (

            settled

            / len(self.transactions)

            * 100

        )

    def total_volume_usd(self) -> float:

        usd = self.transactions[
            self.transactions["currency"]
            .astype(str)
            .str.upper()
            == "USD"
        ]

        return float(

            usd["amount"].sum()

        )

    def total_volume_zwg(self) -> float:

        zwg = self.transactions[
            self.transactions["currency"]
            .astype(str)
            .str.upper()
            == "ZWG"
        ]

        return float(

            zwg["amount"].sum()

        )

    def average_settlement_lag(self) -> float:
        """
        Average days between transaction initiation
        and settlement value date.
        """

        merged = self.transactions.merge(

            self.settlements[

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