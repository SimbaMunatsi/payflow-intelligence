"""
API Schemas.

Pydantic models used by the API.
"""

from pydantic import BaseModel


class PipelineResponse(BaseModel):

    status: str

    duration_seconds: float

    quality_score: int

    warehouse_tables: int