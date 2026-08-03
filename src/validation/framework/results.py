"""
Validation result models.

Author: Simba Munatsi
Project: PayFlow Intelligence Platform
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass
class ValidationResult:
    """
    Represents the outcome of one validation rule.
    """

    rule_name: str

    dataset: str

    passed: bool

    severity: str

    message: str

    rows_affected: int = 0

    recommendation: str = ""

    details: dict[str, Any] = field(default_factory=dict)

    execution_time_ms: float = 0.0

    executed_at: datetime = field(default_factory=datetime.utcnow)

    def to_dict(self):

        return {

            "rule_name": self.rule_name,

            "dataset": self.dataset,

            "passed": self.passed,

            "severity": self.severity,

            "message": self.message,

            "rows_affected": self.rows_affected,

            "recommendation": self.recommendation,

            "execution_time_ms": round(
                self.execution_time_ms,
                2,
            ),

            "executed_at": self.executed_at.isoformat(),

            "details": self.details,
        }