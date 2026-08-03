"""
Generic data cleaning engine.

Performs dataset-independent cleaning operations that
make data safe for downstream processing without
changing its business meaning.

Author: Simba Munatsi
Project: PayFlow Intelligence Platform
"""

from __future__ import annotations

import pandas as pd

from src.utils.logger import get_logger


from time import perf_counter

from src.transformation.results import TransformationResult


logger = get_logger(__name__)


class DataCleaner:
    """
    Generic cleaning engine.

    The cleaner performs operations that are applicable
    to every dataset in the platform.
    """

    def clean(
        self,
        dataset_name: str,
        dataframe: pd.DataFrame,
    ):
        """
        Execute the cleaning pipeline.

        Returns
        -------
        tuple[pd.DataFrame, list[TransformationResult]]
        """

        df = dataframe.copy()

        results = []

        logger.info(f"Cleaning {dataset_name}")

        start = perf_counter()

        before = df.copy()

        df = self.remove_duplicate_columns(df)
        df = self.trim_whitespace(df)
        df = self.standardize_missing_values(df)

        duration = (perf_counter() - start) * 1000

        values_changed = (
            before.astype(str)
            .ne(df.astype(str))
            .sum()
            .sum()
        )

        results.append(
            TransformationResult(
                stage="Transformation",
                operation="Cleaning",
                dataset=dataset_name,
                success=True,
                records_processed=len(df),
                values_changed=int(values_changed),
                execution_time_ms=duration,
            )
        )

        logger.info(
            f"Cleaning completed ({values_changed} values changed)"
        )

        return df, results

    def remove_duplicate_columns(
        self,
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Remove duplicated column names.
        """

        before = len(dataframe.columns)

        dataframe = dataframe.loc[:, ~dataframe.columns.duplicated()]

        removed = before - len(dataframe.columns)

        if removed > 0:
            logger.warning(
                f"Removed {removed} duplicate column(s)"
            )

        return dataframe

    def trim_whitespace(
        self,
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Remove leading/trailing whitespace from
        all string columns.
        """

        object_columns = dataframe.select_dtypes(
            include="object"
        ).columns

        for column in object_columns:

            dataframe[column] = (
                dataframe[column]
                .astype("string")
                .str.strip()
            )

        return dataframe

    def standardize_missing_values(
        self,
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Convert empty strings and common placeholders
        into pandas missing values.
        """

        replacements = {
            "": pd.NA,
            " ": pd.NA,
            "NULL": pd.NA,
            "null": pd.NA,
            "N/A": pd.NA,
            "n/a": pd.NA,
            "None": pd.NA,
            "none": pd.NA,
        }

        dataframe = dataframe.replace(replacements)

        return dataframe