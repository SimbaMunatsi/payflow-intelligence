"""
Executive Business Charts.

Builds business chart datasets from the
analytics warehouse.

Author: Simba Munatsi
Project: PayFlow Intelligence Platform
"""

import pandas as pd

from src.services.executive_dashboard.models import (
    ChartData,
)

from src.utils.logger import get_logger
from src.utils.paths import WAREHOUSE_DATA_DIR

logger = get_logger(__name__)


class ExecutiveChartsBuilder:
    """
    Builds executive dashboard charts.
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

    def build(self) -> list[ChartData]:
        """
        Build all executive charts.
        """

        logger.info(
            "Building executive charts."
        )

        return [

            self.transaction_volume_by_rail(),

            self.transaction_status_distribution(),

            self.payment_volume_by_currency(),

            self.settlement_value_by_rail(),

            self.support_tickets_by_status(),

        ]

    # =====================================================
    # Chart 1
    # =====================================================

    def transaction_volume_by_rail(
        self,
    ) -> ChartData:

        data = (

            self.transactions

            .groupby("rail")

            .size()

            .sort_values(
                ascending=False
            )

        )

        return ChartData(

            title="Transaction Volume by Rail",

            labels=data.index.astype(str).tolist(),

            values=data.values.tolist(),

            chart_type="bar",

        )

    # =====================================================
    # Chart 2
    # =====================================================

    def transaction_status_distribution(
        self,
    ) -> ChartData:

        data = (

            self.transactions

            ["status"]

            .astype(str)

            .str.upper()

            .value_counts()

        )

        return ChartData(

            title="Transaction Status Distribution",

            labels=data.index.tolist(),

            values=data.values.tolist(),

            chart_type="pie",

        )

    # =====================================================
    # Chart 3
    # =====================================================

    def payment_volume_by_currency(
        self,
    ) -> ChartData:

        data = (

            self.transactions

            .assign(

                currency=lambda df:

                df["currency"]

                .astype(str)

                .str.upper()

            )

            .groupby("currency")

            ["amount"]

            .sum()

        )

        return ChartData(

            title="Payment Volume by Currency",

            labels=data.index.tolist(),

            values=data.values.tolist(),

            chart_type="bar",

        )

    # =====================================================
    # Chart 4
    # =====================================================

    def settlement_value_by_rail(
        self,
    ) -> ChartData:

        data = (

            self.settlements

            .groupby("rail")

            ["net_amount"]

            .sum()

            .sort_values(
                ascending=False
            )

        )

        return ChartData(

            title="Settlement Value by Rail",

            labels=data.index.astype(str).tolist(),

            values=data.values.tolist(),

            chart_type="bar",

        )

    # =====================================================
    # Chart 5
    # =====================================================

    def support_tickets_by_status(
        self,
    ) -> ChartData:

        data = (

            self.tickets

            ["status"]

            .astype(str)

            .str.upper()

            .value_counts()

        )

        return ChartData(

            title="Support Tickets by Status",

            labels=data.index.tolist(),

            values=data.values.tolist(),

            chart_type="pie",

        )