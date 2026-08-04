"""
FastAPI Application.

Entry point for the PayFlow Intelligence API.

Author: Simba Munatsi
Project: PayFlow Intelligence Platform
"""

from fastapi import FastAPI

from src.api.routes.health import router as health_router
from src.api.routes.pipeline import router as pipeline_router

app = FastAPI(

    title="PayFlow Intelligence API",

    description=(
        "Backend API for the PayFlow Intelligence Platform."
    ),

    version="1.0.0",

)

app.include_router(
    health_router
)

app.include_router(
     pipeline_router
 )


@app.get("/")
def root():

    return {

        "application": "PayFlow Intelligence Platform",

        "version": "1.0.0",

        "status": "running",

    }