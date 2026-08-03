"""
Transformation result models.

Represents the outcome of a transformation operation
such as cleaning or standardization.

Author: Simba Munatsi
Project: PayFlow Intelligence Platform
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass
class TransformationResult:
    """
    Represents the result of one transformation stage.
    """

    stage: str

    operation: str

    dataset: str

    success: bool

    records_processed: int

    values_changed: int = 0

    execution_time_ms: float = 0.0

    details: dict[str, Any] = field(default_factory=dict)

    executed_at: datetime = field(default_factory=datetime.utcnow)

    def to_dict(self) -> dict:
        """
        Convert the result into a dictionary for
        reporting or persistence.
        """

        return {
            "stage": self.stage,
            "operation": self.operation,
            "dataset": self.dataset,
            "success": self.success,
            "records_processed": self.records_processed,
            "values_changed": self.values_changed,
            "execution_time_ms": round(
                self.execution_time_ms,
                2,
            ),
            "executed_at": self.executed_at.isoformat(),
            "details": self.details,
        }