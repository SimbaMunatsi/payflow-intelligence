"""
Pipeline history tracking.

Author: Simba Munatsi
"""

import pandas as pd

from src.utils.paths import METADATA_DIR


class PipelineHistory:

    FILE = METADATA_DIR / "ingestion_history.csv"

    @classmethod
    def save(cls, metadata_list):

        records = [m.to_dict() for m in metadata_list]

        df = pd.DataFrame(records)

        if cls.FILE.exists():

            existing = pd.read_csv(cls.FILE)

            df = pd.concat(
                [existing, df],
                ignore_index=True,
            )

        df.to_csv(
            cls.FILE,
            index=False,
        )