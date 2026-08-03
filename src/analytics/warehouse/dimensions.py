"""
Warehouse Dimension Builder.

Builds dimension tables for the analytics warehouse.

Author: Simba Munatsi
Project: PayFlow Intelligence Platform
"""

from datetime import timedelta
from time import perf_counter

import pandas as pd

from src.analytics.warehouse.models import WarehouseResult
from src.transformation.metadata_registry import PAYMENT_RAILS
from src.utils.logger import get_logger
from src.utils.paths import WAREHOUSE_DATA_DIR

logger = get_logger(__name__)


class DimensionBuilder:
    """
    Builds warehouse dimension tables.
    """

    def build(
        self,
        datasets: dict[str, pd.DataFrame],
    ) -> tuple[dict[str, pd.DataFrame], list[WarehouseResult]]:

        logger.info("=" * 60)
        logger.info("BUILDING DIMENSIONS")
        logger.info("=" * 60)

        dimensions = {}

        results = []

        builders = [

            self.build_merchants,

            self.build_payment_rails,

            self.build_dates,

        ]

        for builder in builders:

            dataframe, result = builder(datasets)

            dimensions[result.table_name] = dataframe

            results.append(result)

        return dimensions, results

    # -----------------------------------------------------
    # Merchant Dimension
    # -----------------------------------------------------

    def build_merchants(
        self,
        datasets,
    ):

        start = perf_counter()

        df = datasets["merchants"].copy()

        columns = [

            "merchant_id",

            "merchant_name",

            "segment",

            "monthly_volume_band",

        ]

        df = df[columns].drop_duplicates()

        output = (
            WAREHOUSE_DATA_DIR
            / "dim_merchants.parquet"
        )

        df.to_parquet(
            output,
            index=False,
        )

        duration = perf_counter() - start

        logger.info(
            f"Built dim_merchants ({len(df):,} rows)"
        )

        result = WarehouseResult(

            table_name="dim_merchants",

            table_type="Dimension",

            rows=len(df),

            columns=len(df.columns),

            output_path=output,

            successful=True,

            duration_seconds=duration,

            message="Merchant dimension created.",

        )

        return df, result

    # -----------------------------------------------------
    # Payment Rail Dimension
    # -----------------------------------------------------

    def build_payment_rails(
        self,
        datasets,
    ):

        start = perf_counter()

        rows = []

        for rail, metadata in PAYMENT_RAILS.items():

            rows.append({

                "rail": rail,

                "settlement_lag_days":
                    metadata["settlement_lag_days"],

                "charge_rate":
                    metadata["charge_rate"],

            })

        df = pd.DataFrame(rows)

        output = (
            WAREHOUSE_DATA_DIR
            / "dim_payment_rails.parquet"
        )

        df.to_parquet(
            output,
            index=False,
        )

        duration = perf_counter() - start

        logger.info(
            f"Built dim_payment_rails ({len(df)} rows)"
        )

        result = WarehouseResult(

            table_name="dim_payment_rails",

            table_type="Dimension",

            rows=len(df),

            columns=len(df.columns),

            output_path=output,

            successful=True,

            duration_seconds=duration,

            message="Payment rail dimension created.",

        )

        return df, result

    # -----------------------------------------------------
    # Date Dimension
    # -----------------------------------------------------

    def build_dates(
        self,
        datasets,
    ):

        start = perf_counter()

        transactions = datasets["transactions"]

        min_date = (
            transactions["initiated_at"]
            .min()
            .normalize()
        )

        max_date = (
            transactions["initiated_at"]
            .max()
            .normalize()
        )

        dates = []

        current = min_date

        while current <= max_date:

            dates.append({

                "date_key":
                    int(current.strftime("%Y%m%d")),

                "date": current,

                "day":
                    current.day,

                "month":
                    current.month,

                "year":
                    current.year,

                "quarter":
                    current.quarter,

                "weekday":
                    current.day_name(),

                "week":
                    current.isocalendar().week,

                "is_weekend":
                    current.weekday() >= 5,

            })

            current += timedelta(days=1)

        df = pd.DataFrame(dates)

        output = (
            WAREHOUSE_DATA_DIR
            / "dim_dates.parquet"
        )

        df.to_parquet(
            output,
            index=False,
        )

        duration = perf_counter() - start

        logger.info(
            f"Built dim_dates ({len(df)} rows)"
        )

        result = WarehouseResult(

            table_name="dim_dates",

            table_type="Dimension",

            rows=len(df),

            columns=len(df.columns),

            output_path=output,

            successful=True,

            duration_seconds=duration,

            message="Date dimension created.",

        )

        return df, result