"""
Dashboard Models.

Models used by the Pipeline Control Center.

Author: Simba Munatsi
Project: PayFlow Intelligence Platform
"""

from dataclasses import dataclass, field
from src.services.executive_dashboard.models import (
    ExecutiveDashboard,
)

# =====================================================
# KPI Models
# =====================================================

@dataclass
class KPIModel:
    """
    Executive KPI cards displayed
    at the top of the dashboard.
    """

    quality_score: float

    rows_processed: int

    warehouse_tables: int

    execution_time: float


# =====================================================
# Pipeline Models
# =====================================================

@dataclass
class PipelineStage:

    name: str

    status: str


@dataclass
class PipelineStatus:

    stages: list[PipelineStage] = field(
        default_factory=list
    )


# =====================================================
# Data Quality
# =====================================================

@dataclass
class QualityCategory:
    """
    Data quality statistics for a validation category.
    """

    name: str

    total: int

    passed: int

    failed: int

    pass_rate: float


@dataclass
class QualitySection:

    overall_score: float

    categories: list[
        QualityCategory
    ] = field(default_factory=list)


# =====================================================
# Warehouse
# =====================================================

@dataclass
class WarehouseTable:

    name: str

    rows: int

    table_type: str


@dataclass
class WarehouseSection:

    tables: list[
        WarehouseTable
    ] = field(default_factory=list)


# =====================================================
# Summary
# =====================================================

@dataclass
class SummarySection:

    datasets_loaded: int

    validation_rules: int

    rules_passed: int

    rules_failed: int

    run_timestamp: str


# =====================================================
# Dashboard
# =====================================================

@dataclass
class DashboardResponse:
    """
    Complete dashboard model.
    """

    status: str

    executive: ExecutiveDashboard

    kpis: KPIModel

    pipeline: PipelineStatus

    quality: QualitySection

    warehouse: WarehouseSection

    summary: SummarySection