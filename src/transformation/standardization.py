"""
Generic data standardization engine.

Applies dataset-specific standardization rules using
the schema registry.

Author: Simba Munatsi
Project: PayFlow Intelligence Platform
"""

import pandas as pd

from src.transformation.metadata_registry import METADATA_REGISTRY
from src.utils.logger import get_logger
from time import perf_counter
from src.transformation.results import TransformationResult

logger = get_logger(__name__)


class DataStandardizer:
    """
    Standardizes cleaned datasets.
    """

    def standardize(
        self,
        dataset_name: str,
        dataframe: pd.DataFrame,
    ):
        """
        Standardize a cleaned dataset.

        Returns
        -------
        tuple[pd.DataFrame, list[TransformationResult]]
        """

        df = dataframe.copy()

        logger.info(f"Standardizing {dataset_name}")

        schema = METADATA_REGISTRY.get(
            dataset_name,
            {},
        )

        start = perf_counter()

        before = df.copy()

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

        duration = (perf_counter() - start) * 1000

        values_changed = (
            before.astype(str)
            .ne(df.astype(str))
            .sum()
            .sum()
        )

        result = TransformationResult(
            stage="Transformation",
            operation="Standardization",
            dataset=dataset_name,
            success=True,
            records_processed=len(df),
            values_changed=int(values_changed),
            execution_time_ms=duration,
        )

        logger.info(
            f"{dataset_name} standardized "
            f"({values_changed} values changed)"
        )

        return df, [result]

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