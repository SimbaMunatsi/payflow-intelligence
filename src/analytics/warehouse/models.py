"""
Warehouse Models.

Models used by the Analytics Warehouse layer.

Author: Simba Munatsi
Project: PayFlow Intelligence Platform
"""

from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any


@dataclass
class WarehouseResult:
    """
    Result of building a single warehouse table.
    """

    table_name: str

    table_type: str
    # "Dimension" or "Fact"

    rows: int

    columns: int

    output_path: Path

    successful: bool

    duration_seconds: float

    message: str = ""

    metadata: dict[str, Any] = field(default_factory=dict)

    created_at: datetime = field(
        default_factory=datetime.utcnow
    )

    def to_dict(self):

        return {

            "table_name": self.table_name,

            "table_type": self.table_type,

            "rows": self.rows,

            "columns": self.columns,

            "output_path": str(
                self.output_path
            ),

            "successful": self.successful,

            "duration_seconds": round(
                self.duration_seconds,
                3,
            ),

            "message": self.message,

            "metadata": self.metadata,

            "created_at": self.created_at.isoformat(),

        }


@dataclass
class WarehouseSummary:
    """
    Overall warehouse build summary.
    """

    total_tables: int

    successful: int

    failed: int

    duration_seconds: float

    tables: list[WarehouseResult] = field(
        default_factory=list
    )

    @property
    def success_rate(self) -> float:

        if self.total_tables == 0:

            return 0.0

        return round(

            self.successful

            / self.total_tables

            * 100,

            2,

        )

    def to_dict(self):

        return {

            "total_tables": self.total_tables,

            "successful": self.successful,

            "failed": self.failed,

            "duration_seconds": round(
                self.duration_seconds,
                3,
            ),

            "success_rate": self.success_rate,

            "tables": [
                table.to_dict()
                for table in self.tables
            ],

        }