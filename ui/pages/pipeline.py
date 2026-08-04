"""
Pipeline Page.

Pipeline monitoring dashboard for the
PayFlow Intelligence Platform.

Author: Simba Munatsi
Project: PayFlow Intelligence Platform
"""

import streamlit as st

from components.api import run_pipeline


def render():
    """
    Render the Pipeline page.
    """

    st.header("⚙ Pipeline Monitoring")

    st.caption(
        "Monitor pipeline execution and operational status."
    )

    st.divider()

    if st.button(
        "▶ Run Pipeline",
        use_container_width=True,
        key="pipeline_run_button",
    ):

        with st.spinner(
            "Executing pipeline..."
        ):

            result = run_pipeline()

        st.success(
            "Pipeline completed successfully."
        )

        render_pipeline(result)


# =====================================================
# Pipeline Dashboard
# =====================================================

def render_pipeline(result: dict):

    kpis = result["kpis"]

    pipeline = result["pipeline"]

    summary = result["summary"]

    # =====================================================
    # Execution Statistics
    # =====================================================

    st.subheader("📈 Execution Statistics")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "Execution Time",
            f"{kpis['execution_time']:.2f}s",
        )

    with col2:

        st.metric(
            "Rows Processed",
            f"{kpis['rows_processed']:,}",
        )

    with col3:

        st.metric(
            "Datasets",
            summary["datasets_loaded"],
        )

    with col4:

        st.metric(
            "Validation Rules",
            summary["validation_rules"],
        )

    st.divider()

    # =====================================================
    # Pipeline Flow
    # =====================================================

    st.subheader("🔄 Pipeline Flow")

    stages = pipeline["stages"]

    cols = st.columns(len(stages))

    for col, stage in zip(cols, stages):

        with col:

            if stage["status"] == "Completed":

                st.success(stage["name"])

            else:

                st.error(stage["name"])

            st.caption(stage["status"])

    st.divider()

    # =====================================================
    # Latest Pipeline Run
    # =====================================================

    st.subheader("📝 Latest Pipeline Run")

    left, right = st.columns(2)

    with left:

        st.markdown(f"""
**Status**

{result["status"].upper()}

**Run Timestamp**

{summary["run_timestamp"]}

**Datasets Loaded**

{summary["datasets_loaded"]}
""")

    with right:

        st.markdown(f"""
**Validation Rules**

{summary["validation_rules"]}

**Rows Processed**

{kpis["rows_processed"]:,}

**Execution Time**

{kpis["execution_time"]:.2f} seconds
""")

