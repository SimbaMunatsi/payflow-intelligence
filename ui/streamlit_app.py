"""
PayFlow Intelligence
Pipeline Control Center

Author: Simba Munatsi
"""

import requests
import streamlit as st

API_URL = "http://127.0.0.1:8000"

st.set_page_config(

    page_title="PayFlow Intelligence",

    page_icon="📊",

    layout="wide",

)

# =====================================================
# Title
# =====================================================

st.title("📊 PayFlow Intelligence")

st.caption(
    "Pipeline Control Center"
)

st.divider()

# =====================================================
# API Health
# =====================================================

try:

    health = requests.get(
        f"{API_URL}/health",
        timeout=5,
    )

    if health.status_code == 200:

        st.success(
            "API Connected"
        )

    else:

        st.error(
            "API Unavailable"
        )

except Exception:

    st.error(
        "Cannot connect to API"
    )

st.divider()

# =====================================================
# Run Pipeline
# =====================================================

if st.button(

    "▶ Run Pipeline",

    use_container_width=True,

):

    with st.spinner(
        "Running pipeline..."
    ):

        response = requests.post(
            f"{API_URL}/pipeline/run",
            timeout=300,
        )

    if response.status_code == 200:

        result = response.json()

        st.success(
            "Pipeline completed successfully."
        )

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(

                "Quality Score",

                result["quality_score"],

            )

        with col2:

            st.metric(

                "Warehouse Tables",

                result["warehouse_tables"],

            )

        with col3:

            st.metric(

                "Execution Time",

                f'{result["duration_seconds"]:.2f}s',

            )

        st.divider()

        st.subheader(
            "Latest Pipeline Run"
        )

        st.json(result)

    else:

        st.error(
            "Pipeline execution failed."
        )