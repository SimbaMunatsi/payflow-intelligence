"""
Reports Page.

Displays available operational reports.

Author: Simba Munatsi
Project: PayFlow Intelligence Platform
"""

import json

import streamlit as st

from components.api import run_pipeline


def render():
    """
    Render the Reports page.
    """

    st.header("📄 Reports")

    st.caption(
        "Generate and download operational reports."
    )

    st.divider()

    if st.button(
        "🔄 Generate Latest Reports",
        width="stretch",
        key="reports_generate_button",
    ):

        with st.spinner(
            "Generating reports..."
        ):

            result = run_pipeline()

        render_reports(result)


# =====================================================
# Reports Dashboard
# =====================================================

def render_reports(result):

    st.success(
        "Reports generated successfully."
    )

    st.subheader(
        "Available Reports"
    )

    report1, report2 = st.columns(2)

    # =====================================================
    # Pipeline Summary Report
    # =====================================================

    with report1:

        st.markdown(
            "### 📊 Pipeline Summary"
        )

        st.caption(
            "Overall pipeline execution summary."
        )

        st.download_button(

            label="Download JSON",

            data=json.dumps(
                result,
                indent=4,
            ),

            file_name="pipeline_summary.json",

            mime="application/json",

            width="stretch",

        )

    # =====================================================
    # Validation Report
    # =====================================================

    with report2:

        st.markdown(
            "### 📈 Validation Report"
        )

        st.caption(
            "Detailed validation report."
        )

        st.info(
            "CSV export coming soon."
        )

    st.divider()

    report3, report4 = st.columns(2)

    # =====================================================
    # Warehouse Report
    # =====================================================

    with report3:

        st.markdown(
            "### 🏢 Warehouse Report"
        )

        st.caption(
            "Warehouse inventory and table statistics."
        )

        st.info(
            "CSV export coming soon."
        )

    # =====================================================
    # Executive Report
    # =====================================================

    with report4:

        st.markdown(
            "### 📑 Executive Report"
        )

        st.caption(
            "Business-ready operational summary."
        )

        st.info(
            "PDF report coming soon."
        )

    st.divider()

    st.subheader(
        "Latest Pipeline Summary"
    )

    kpis = result["kpis"]

    summary = result["summary"]

    left, right = st.columns(2)

    with left:

        st.metric(
            "Quality Score",
            f"{kpis['quality_score']}%"
        )

        st.metric(
            "Rows Processed",
            f"{kpis['rows_processed']:,}"
        )

        st.metric(
            "Warehouse Tables",
            kpis["warehouse_tables"]
        )

    with right:

        st.metric(
            "Rules Passed",
            summary["rules_passed"]
        )

        st.metric(
            "Rules Failed",
            summary["rules_failed"]
        )

        st.metric(
            "Datasets Loaded",
            summary["datasets_loaded"]
        )