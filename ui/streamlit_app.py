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

        # =====================================================
        # KPI Metrics
        # =====================================================

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(

                "Quality Score",

                f"{result['quality_score']}%",

            )

        with col2:

            st.metric(

                "Warehouse Tables",

                result["warehouse_tables"],

            )

        with col3:

            st.metric(

                "Execution Time",

                f"{result['duration_seconds']:.2f}s",

            )

        st.divider()

        # =====================================================
        # Pipeline Stages
        # =====================================================

        st.subheader(
            "Pipeline Stages"
        )

        for stage, status in result["stages"].items():

            if status == "Completed":

                st.success(
                    f"{stage.title()} ✓"
                )

            else:

                st.error(
                    f"{stage.title()} ✗"
                )

        st.divider()

        # =====================================================
        # Pipeline Execution Summary
        # =====================================================

        st.subheader(
            "📋 Pipeline Execution Summary"
        )

        summary_left, summary_right = st.columns(2)

        with summary_left:

            st.markdown(
                f"""
**Run Status**

{result["status"].upper()}

**Execution Time**

{result["duration_seconds"]:.2f} seconds

**Datasets Loaded**

{result["datasets_loaded"]}

**Rows Processed**

{result["rows_processed"]:,}

**Validation Rules**

{result["validation_rules"]}
"""
            )

        with summary_right:

            st.markdown(
                f"""
**Rules Passed**

{result["rules_passed"]}

**Rules Failed**

{result["rules_failed"]}

**Quality Score**

{result["quality_score"]}%

**Warehouse Tables**

{result["warehouse_tables"]}

**Warehouse Success**

{result["warehouse_success_rate"]}%

**Run Timestamp**

{result["run_timestamp"]}
"""
            )

    else:

        st.error(
            "Pipeline execution failed."
        )