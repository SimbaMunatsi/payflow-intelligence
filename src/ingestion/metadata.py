"""
Metadata models for pipeline ingestion.

Author: Simba Munatsi
Project: PayFlow Intelligence Platform
"""

from dataclasses import dataclass
from datetime import datetime
from uuid import uuid4

RUN_ID = str(uuid4())


@dataclass
class DatasetMetadata:
    """
    Stores metadata about an ingested dataset.
    """

    run_id: str
    dataset_name: str
    source_file: str
    rows: int
    columns: int
    load_timestamp: datetime
    file_size_mb: float

    def to_dict(self):
        return {
            "dataset_name": self.dataset_name,
            "source_file": self.source_file,
            "rows": self.rows,
            "columns": self.columns,
            "load_timestamp": self.load_timestamp.isoformat(),
            "file_size_mb": round(self.file_size_mb, 2),
        }


from dataclasses import field

@dataclass
class PipelineSummary:
    """
    Summary of one pipeline stage execution.
    """

    stage: str

    successful: int

    failed: int

    failed_datasets: list[str] = field(default_factory=list)

    duration_seconds: float = 0.0