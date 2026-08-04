"""
Health API.

Simple endpoint used to verify that the
backend is running.
"""

from datetime import datetime, timezone

from fastapi import APIRouter

router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


@router.get("")
def health():

    return {

        "status": "healthy",

        "timestamp": datetime.now(
            timezone.utc
        ).isoformat(),

    }