"""
Pipeline API.

Endpoints for executing the PayFlow Intelligence pipeline.

Author: Simba Munatsi
Project: PayFlow Intelligence Platform
"""

from fastapi import APIRouter, HTTPException
from fastapi import Query

from src.services.dashboard_service import DashboardService
from src.services.pipeline_service import PipelineService

router = APIRouter(
    prefix="/pipeline",
    tags=["Pipeline"],
)

pipeline_service = PipelineService()
dashboard_service = DashboardService()


@router.post("/run")
def run_pipeline(
    start_date: str = Query(
        None,
        description="Start date for the pipeline execution (YYYY-MM-DD).",
    ),
    end_date: str = Query(
        None,
        description="End date for the pipeline execution (YYYY-MM-DD).",
    ),
):
    """
    Execute the PayFlow Intelligence pipeline and
    return the dashboard model.
    """

    try:

        pipeline_result = (
            pipeline_service.run_pipeline()
        )

        dashboard = (
            dashboard_service.build_dashboard(
                pipeline_result,
                start_date=start_date,
                end_date=end_date,
            )
        )

        return dashboard

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=f"Pipeline execution failed: {str(ex)}",
        ) from ex

@router.get(
    "/history",
)
def get_pipeline_history():
    """
    Return pipeline execution history.
    """

    try:

        return pipeline_service.get_history()

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=f"History endpoint failed: {str(ex)}",
        ) from ex    