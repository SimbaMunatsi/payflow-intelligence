"""
API Client.

Handles communication with the
PayFlow Intelligence API.

Author: Simba Munatsi
"""

import requests

API_URL = "http://127.0.0.1:8000"


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


def run_pipeline():
    """
    Execute the pipeline.
    """

    response = requests.post(
        f"{API_URL}/pipeline/run",
        timeout=300,
    )

    response.raise_for_status()

    return response.json()

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