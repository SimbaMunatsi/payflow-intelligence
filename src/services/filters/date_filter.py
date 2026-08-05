"""
Date Filter Service.

Filters warehouse datasets by a selected
date range.

Author: Simba Munatsi
Project: PayFlow Intelligence Platform
"""

import pandas as pd

from src.utils.logger import get_logger

logger = get_logger(__name__)


class DateFilter:
    """
    Filters warehouse datasets using
    a date range.
    """

    @staticmethod
    def filter(
        dataframe: pd.DataFrame,
        date_column: str,
        start_date=None,
        end_date=None,
    ) -> pd.DataFrame:
        """
        Filter a dataframe using the
        supplied date range.
        """

        if dataframe.empty:

            return dataframe

        df = dataframe.copy()

        df[date_column] = pd.to_datetime(
            df[date_column]
        )

        if start_date is not None:

            start_date = pd.to_datetime(
                start_date
            )

            df = df[
                df[date_column] >= start_date
            ]

        if end_date is not None:

            end_date = pd.to_datetime(
                end_date
            )

            df = df[
                df[date_column] <= end_date
            ]

        logger.info(

            "Date filter applied: %s -> %s (%s rows)",

            start_date,

            end_date,

            len(df),

        )

        return df