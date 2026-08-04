"""
API Schemas.

Pydantic models used by the API.
"""

from typing import Dict

from pydantic import BaseModel


class PipelineResponse(BaseModel):

    status: str

    duration_seconds: float

    quality_score: int

    warehouse_tables: int

    warehouse_success_rate: float

    datasets_loaded: int

    validation_rules: int

    rules_passed: int

    rules_failed: int

    rows_processed: int

    run_timestamp: str

    stages: Dict[str, str]