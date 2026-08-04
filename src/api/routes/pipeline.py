"""
Pipeline API.

Endpoints for executing the PayFlow Intelligence pipeline.

Author: Simba Munatsi
Project: PayFlow Intelligence Platform
"""

from fastapi import APIRouter, HTTPException

from src.api.schemas import PipelineResponse
from src.services.pipeline_service import PipelineService

router = APIRouter(
    prefix="/pipeline",
    tags=["Pipeline"],
)

pipeline_service = PipelineService()


@router.post(
    "/run",
    response_model=PipelineResponse,
)
def run_pipeline():
    """
    Execute the complete PayFlow Intelligence pipeline.
    """

    try:

        result = pipeline_service.run_pipeline()

        return PipelineResponse(**result)

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=f"Pipeline execution failed: {str(ex)}",
        ) from ex