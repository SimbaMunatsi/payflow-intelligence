"""
Dataset ingestion service.

Author: Simba Munatsi
Project: PayFlow Intelligence Platform
"""

from datetime import datetime
from pathlib import Path

import pandas as pd
import time

from src.ingestion.history import PipelineHistory
from src.ingestion.metadata import (
    DatasetMetadata,
    RUN_ID,
    PipelineSummary,
)
from src.utils.logger import get_logger
from src.utils.paths import LANDING_DATA_DIR, RAW_DATA_DIR


logger = get_logger(__name__)


class DataLoader:
    """
    Handles ingestion of raw datasets into the Landing Layer.
    """

    def __init__(self):
        self.metadata = []

    def discover_files(self):
        """
        Find all CSV files in the raw directory.
        """
        return sorted(RAW_DATA_DIR.glob("*.csv"))

    def load_dataset(self, file_path: Path):
        """
        Load a single CSV dataset.
        """

        logger.info(f"Loading {file_path.name}")

        df = pd.read_csv(file_path)

        metadata = DatasetMetadata(
            run_id=RUN_ID,
            dataset_name=file_path.stem,
            source_file=file_path.name,
            rows=len(df),
            columns=len(df.columns),
            load_timestamp=datetime.now(),
            file_size_mb=file_path.stat().st_size / (1024 * 1024),
        )

        self.metadata.append(metadata)

        logger.info(
            f"{file_path.name} loaded successfully "
            f"({metadata.rows:,} rows)"
        )

        return df, metadata

    def save_to_landing(self, dataframe, dataset_name):
        """
        Save dataframe to landing layer as parquet.
        """

        output_path = LANDING_DATA_DIR / f"{dataset_name}.parquet"

        dataframe.to_parquet(
            output_path,
            index=False,
            engine="pyarrow",
        )

        logger.info(f"Saved {output_path.name}")

    def run(self):
        """
        Run ingestion for every dataset.
        """

        start = time.perf_counter()

        datasets = {}

        successful = 0

        failed = 0

        failed_datasets = []

        files = self.discover_files()

        logger.info(f"Discovered {len(files)} datasets.")

        for file in files:

            try:

                df, metadata = self.load_dataset(file)

                self.save_to_landing(
                    df,
                    metadata.dataset_name,
                )

                datasets[metadata.dataset_name] = df

                successful += 1

            except Exception:

                logger.exception(
                    f"Failed loading {file.name}"
                )

                failed += 1

                failed_datasets.append(file.name)

        duration = time.perf_counter() - start

        summary = PipelineSummary(
            stage="Landing",
            successful=successful,
            failed=failed,
            failed_datasets=failed_datasets,
            duration_seconds=duration,
        )

        logger.info(
            f"Landing completed "
            f"(Success={successful}, Failed={failed})"
        )

        return datasets, self.metadata, summary