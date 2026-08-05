"""
API Client.

Handles communication with the
PayFlow Intelligence API.

Author: Simba Munatsi
"""

import os
import requests

API_URL = os.getenv(

    "API_URL",

    "http://127.0.0.1:8000",

)


def get_health():
    """
    Check API health.
    """

    try:

        response = requests.get(
            f"{API_URL}/health",
            timeout=5,
        )

        return response.status_code == 200

    except Exception:

        return False


def get_dashboard(
    start_date=None,
    end_date=None,
):
    """
    Execute the pipeline and return the
    complete dashboard.
    """

    params = {}

    if start_date:

        params["start_date"] = str(
            start_date
        )

    if end_date:

        params["end_date"] = str(
            end_date
        )

    response = requests.post(

        f"{API_URL}/pipeline/run",

        params=params,

        timeout=300,

    )

    response.raise_for_status()

    return response.json()


# Backwards compatibility
run_pipeline = get_dashboard


# Backwards compatibility
run_pipeline = get_dashboard

def get_pipeline_history():
    """
    Fetch pipeline history.
    """

    response = requests.get(

        f"{API_URL}/pipeline/history",

        timeout=30,

    )

    response.raise_for_status()

    return response.json()