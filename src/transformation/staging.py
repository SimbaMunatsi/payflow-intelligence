"""
Staging Engine.

Transforms landing datasets into trusted staging datasets.

Author: Simba Munatsi
Project: PayFlow Intelligence Platform
"""

from pathlib import Path

import pandas as pd

from src.transformation.cleaning import DataCleaner
from src.transformation.standardization import DataStandardizer
from src.transformation.results import TransformationResult
from src.utils.logger import get_logger
from src.utils.paths import STAGING_DATA_DIR

logger = get_logger(__name__)


class StagingEngine:
    """
    Creates standardized staging datasets.
    """

    def __init__(self):

        self.cleaner = DataCleaner()

        self.standardizer = DataStandardizer()

    def process_dataset(
        self,
        dataset_name: str,
        dataframe: pd.DataFrame,
    ):
        """
        Process a single dataset.

        Returns
        -------
        tuple[pd.DataFrame, list[TransformationResult]]
        """

        logger.info(f"Processing {dataset_name}")

        results = []

        # Cleaning
        cleaned_df, cleaning_results = self.cleaner.clean(
            dataset_name,
            dataframe,
        )

        results.extend(cleaning_results)

        # Standardization
        standardized_df, standardization_results = (
            self.standardizer.standardize(
                dataset_name,
                cleaned_df,
            )
        )

        results.extend(standardization_results)

        # Save to staging
        output_path = (
            STAGING_DATA_DIR /
            f"{dataset_name}.parquet"
        )

        standardized_df.to_parquet(
            output_path,
            index=False,
            engine="pyarrow",
        )

        logger.info(
            f"Saved staging dataset: {output_path.name}"
        )

        return standardized_df, results

    def run(
        self,
        datasets: dict[str, pd.DataFrame],
    ):
        """
        Process all datasets.

        Parameters
        ----------
        datasets
            Landing datasets.

        Returns
        -------
        tuple[
            dict[str, pd.DataFrame],
            list[TransformationResult]
        ]
        """

        staging_datasets = {}

        transformation_results = []

        logger.info("=" * 60)
        logger.info("STARTING STAGING LAYER")
        logger.info("=" * 60)

        for dataset_name, dataframe in datasets.items():

            staged_df, results = self.process_dataset(
                dataset_name,
                dataframe,
            )

            staging_datasets[dataset_name] = staged_df

            transformation_results.extend(results)

        logger.info("=" * 60)
        logger.info("STAGING LAYER COMPLETED")
        logger.info("=" * 60)

        return (
            staging_datasets,
            transformation_results,
        )