"""
Warehouse Fact Builder.

Builds fact tables for the analytics warehouse.

Author: Simba Munatsi
Project: PayFlow Intelligence Platform
"""

from datetime import datetime, timezone
from time import perf_counter

import pandas as pd

from src.analytics.warehouse.models import WarehouseResult
from src.utils.logger import get_logger
from src.utils.paths import WAREHOUSE_DATA_DIR

logger = get_logger(__name__)


class FactBuilder:
    """
    Builds warehouse fact tables.
    """

    def build(
        self,
        datasets: dict[str, pd.DataFrame],
    ) -> tuple[dict[str, pd.DataFrame], list[WarehouseResult]]:

        logger.info("=" * 60)
        logger.info("BUILDING FACT TABLES")
        logger.info("=" * 60)

        facts = {}
        results = []

        builders = [
            self.build_transactions,
            self.build_settlements,
            self.build_support_tickets,
        ]

        for builder in builders:

            dataframe, result = builder(datasets)

            facts[result.table_name] = dataframe

            results.append(result)

        return facts, results

    # =====================================================
    # Utility Methods
    # =====================================================

    def _create_date_key(
        self,
        series: pd.Series,
    ) -> pd.Series:
        """
        Create a nullable YYYYMMDD date key.

        Invalid or missing dates become <NA>.
        """

        series = pd.to_datetime(
            series,
            errors="coerce",
        )

        return (
            pd.to_numeric(
                series.dt.strftime("%Y%m%d"),
                errors="coerce",
            )
            .astype("Int64")
        )

    # =====================================================
    # Transactions Fact
    # =====================================================

    def build_transactions(
        self,
        datasets,
    ):

        start = perf_counter()

        df = datasets["transactions"].copy()

        df["date_key"] = self._create_date_key(
            df["initiated_at"]
        )

        df["etl_loaded_at"] = datetime.now(
            timezone.utc
        )

        columns = [

            "txn_ref",

            "merchant_id",

            "rail",

            "currency",

            "amount",

            "status",

            "attempt_count",

            "rail_latency_ms",

            "initiated_at",

            "authorised_at",

            "date_key",

            "etl_loaded_at",

        ]

        df = df[columns]

        output = (
            WAREHOUSE_DATA_DIR
            / "fact_transactions.parquet"
        )

        df.to_parquet(
            output,
            index=False,
        )

        duration = perf_counter() - start

        logger.info(
            f"Built fact_transactions ({len(df):,} rows)"
        )

        result = WarehouseResult(

            table_name="fact_transactions",

            table_type="Fact",

            rows=len(df),

            columns=len(df.columns),

            output_path=output,

            successful=True,

            duration_seconds=duration,

            message="Transaction fact created.",

        )

        return df, result

    # =====================================================
    # Settlements Fact
    # =====================================================

    def build_settlements(
        self,
        datasets,
    ):

        start = perf_counter()

        df = datasets["settlements"].copy()

        df["date_key"] = self._create_date_key(
            df["value_date"]
        )

        df["etl_loaded_at"] = datetime.now(
            timezone.utc
        )

        columns = [

            "rail_reference",

            "merchant_id",

            "rail",

            "currency",

            "gross_amount",

            "rail_charges",

            "net_amount",

            "line_type",

            "value_date",

            "date_key",

            "etl_loaded_at",

        ]

        df = df[columns]

        output = (
            WAREHOUSE_DATA_DIR
            / "fact_settlements.parquet"
        )

        df.to_parquet(
            output,
            index=False,
        )

        duration = perf_counter() - start

        logger.info(
            f"Built fact_settlements ({len(df):,} rows)"
        )

        result = WarehouseResult(

            table_name="fact_settlements",

            table_type="Fact",

            rows=len(df),

            columns=len(df.columns),

            output_path=output,

            successful=True,

            duration_seconds=duration,

            message="Settlement fact created.",

        )

        return df, result

    # =====================================================
    # Support Tickets Fact
    # =====================================================

    def build_support_tickets(
        self,
        datasets,
    ):

        start = perf_counter()

        df = datasets["tickets"].copy()

        df["date_key"] = self._create_date_key(
            df["opened_at"]
        )

        df["etl_loaded_at"] = datetime.now(
            timezone.utc
        )

        columns = [

            "ticket_id",

            "merchant_id",

            "channel",

            "status",

            "txn_ref",

            "opened_at",

            "date_key",

            "etl_loaded_at",

        ]

        df = df[columns]

        output = (
            WAREHOUSE_DATA_DIR
            / "fact_support_tickets.parquet"
        )

        df.to_parquet(
            output,
            index=False,
        )

        duration = perf_counter() - start

        logger.info(
            f"Built fact_support_tickets ({len(df):,} rows)"
        )

        result = WarehouseResult(

            table_name="fact_support_tickets",

            table_type="Fact",

            rows=len(df),

            columns=len(df.columns),

            output_path=output,

            successful=True,

            duration_seconds=duration,

            message="Support ticket fact created.",

        )

        return df, result