"""
Executive Dashboard API.

Provides business intelligence endpoints.

Author: Simba Munatsi
Project: PayFlow Intelligence Platform
"""

from fastapi import APIRouter, HTTPException

from src.services.executive_dashboard.service import (
    ExecutiveDashboardService,
)

router = APIRouter(

    prefix="/dashboard",

    tags=["Executive Dashboard"],

)

dashboard_service = ExecutiveDashboardService()


@router.get(
    "/executive",
)
def executive_dashboard():
    """
    Return the Executive Operations Dashboard.
    """

    try:

        return dashboard_service.to_dict()

    except Exception as ex:

        raise HTTPException(

            status_code=500,

            detail=str(ex),

        ) from ex