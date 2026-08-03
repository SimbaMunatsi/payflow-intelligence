"""
Pipeline history tracking.

Author: Simba Munatsi
Project: PayFlow Intelligence Platform
"""

import pandas as pd
from pandas.errors import EmptyDataError

from src.utils.logger import get_logger
from src.utils.paths import METADATA_DIR

logger = get_logger(__name__)


class PipelineHistory:
    """
    Maintains a historical record of pipeline ingestion runs.
    """

    FILE = METADATA_DIR / "ingestion_history.csv"

    @classmethod
    def save(cls, metadata_list):
        """
        Append ingestion metadata to the history file.
        """

        records = [m.to_dict() for m in metadata_list]

        new_history = pd.DataFrame(records)

        # --------------------------------------------
        # First run
        # --------------------------------------------

        if not cls.FILE.exists():

            logger.info(
                "Creating ingestion history."
            )

            new_history.to_csv(
                cls.FILE,
                index=False,
            )

            return

        # --------------------------------------------
        # Existing history
        # --------------------------------------------

        try:

            existing = pd.read_csv(
                cls.FILE
            )

        except EmptyDataError:

            logger.warning(
                "History file was empty. "
                "Creating a new history."
            )

            existing = pd.DataFrame()

        updated = pd.concat(
            [
                existing,
                new_history,
            ],
            ignore_index=True,
        )

        updated.to_csv(
            cls.FILE,
            index=False,
        )

        logger.info(
            f"History updated ({len(updated)} total records)."
        )