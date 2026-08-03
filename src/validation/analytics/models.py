"""
Validation Analytics Models.

Models used by the validation analytics layer.

Author: Simba Munatsi
Project: PayFlow Intelligence Platform
"""

from dataclasses import dataclass, field


@dataclass
class DatasetSummary:
    """
    Validation summary for a single dataset.
    """

    dataset: str

    total_rules: int

    passed: int

    failed: int

    critical: int

    errors: int

    warnings: int

    infos: int


@dataclass
class ValidationSummary:
    """
    Overall validation summary.
    """

    total_rules: int

    passed: int

    failed: int

    critical: int

    errors: int

    warnings: int

    infos: int

    datasets: dict[str, DatasetSummary] = field(default_factory=dict)

    categories: dict[str, dict] = field(default_factory=dict)

@dataclass
class DashboardModel:
    """
    Dashboard-ready validation analytics.
    """

    quality_score: float

    summary: ValidationSummary    