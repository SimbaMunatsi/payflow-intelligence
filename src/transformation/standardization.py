"""
Generic data standardization engine.

Applies dataset-specific standardization rules using
the schema registry.

Author: Simba Munatsi
Project: PayFlow Intelligence Platform
"""

import pandas as pd

from src.transformation.metadata_registry import SCHEMA_REGISTRY
from src.utils.logger import get_logger

logger = get_logger(__name__)


class DataStandardizer:
    """
    Standardizes cleaned datasets.
    """

    def standardize(
        self,
        dataset_name: str,
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:

        df = dataframe.copy()

        logger.info(
            f"Standardizing {dataset_name}"
        )

        schema = SCHEMA_REGISTRY.get(
            dataset_name,
            {},
        )

        self._convert_datetimes(
            df,
            schema.get("datetime", []),
        )

        self._convert_numeric(
            df,
            schema.get("numeric", []),
        )

        self._convert_integer(
            df,
            schema.get("integer", []),
        )

        self._uppercase_columns(
            df,
            schema.get("uppercase", []),
        )

        logger.info(
            f"{dataset_name} standardized"
        )

        return df

    def _convert_datetimes(
        self,
        dataframe,
        columns,
    ):

        for column in columns:

            if column in dataframe.columns:

                dataframe[column] = pd.to_datetime(
                    dataframe[column],
                    errors="coerce",
                )

    def _convert_numeric(
        self,
        dataframe,
        columns,
    ):

        for column in columns:

            if column in dataframe.columns:

                dataframe[column] = pd.to_numeric(
                    dataframe[column],
                    errors="coerce",
                )

    def _convert_integer(
        self,
        dataframe,
        columns,
    ):

        for column in columns:

            if column in dataframe.columns:

                dataframe[column] = pd.to_numeric(
                    dataframe[column],
                    errors="coerce",
                ).astype("Int64")

    def _uppercase_columns(
        self,
        dataframe,
        columns,
    ):

        for column in columns:

            if column in dataframe.columns:

                dataframe[column] = (
                    dataframe[column]
                    .astype("string")
                    .str.upper()
                )