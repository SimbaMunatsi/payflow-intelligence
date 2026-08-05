"""
AI Insights Page.

Provides intelligent operational insights based on
pipeline execution results..

Author: Simba Munatsi
Project: PayFlow Intelligence Platform
"""

import streamlit as st

from components.api import run_pipeline


def render():
    """
    Render the AI Insights page.
    """

    st.header("🤖 AI Insights")

    st.caption(
        "AI-powered operational insights and recommendations."
    )

    st.divider()

    if st.button(
        "🧠 Generate Insights",
        width="stretch",
        key="ai_generate_button",
    ):

        with st.spinner(
            "Analysing pipeline...."
        ):

            result = run_pipeline()

        render_insights(result)


# =====================================================
# AI Dashboard
# =====================================================

def render_insights(result):

    quality = result["quality"]

    summary = result["summary"]

    score = quality["overall_score"]

    st.subheader("📈 Overall Health")

    st.metric(
        "Data Quality Score",
        f"{score}%"
    )

    st.progress(score / 100)

    st.divider()

    st.subheader("💡 Operational Insights")

    if score >= 90:

        st.success(
            "Excellent overall data quality. No significant operational issues detected.."
        )

    elif score >= 80:

        st.warning(
            "Data quality is good, but a few validation issues require attention."
        )

    else:

        st.error(
            "Data quality is below the acceptable threshold. Immediate investigation is recommended."
        )

    st.divider()

    st.subheader("📋 Recommendations")

    for category in quality["categories"]:

        if category["failed"] == 0:

            st.success(
                f"{category['name']}: All validation rules passed."
            )

        else:

            st.warning(
                f"{category['name']}: "
                f"{category['failed']} validation rule(s) failed."
            )

    st.divider()

    st.subheader("🚀 Suggested Actions")

    if summary["rules_failed"] > 0:

        st.markdown(
            """
- Review failed validation rules.
- Investigate settlement discrepancies.
- Verify merchant reference integrity.
- Review duplicate transactions.
- Re-run the pipeline after corrections.
"""
        )

    else:

        st.success(
            "No corrective actions are currently required."
        )

    st.divider()

    st.subheader("📊 Executive Summary")

    left, right = st.columns(2)

    with left:

        st.metric(
            "Rules Passed",
            summary["rules_passed"]
        )

        st.metric(
            "Rules Failed",
            summary["rules_failed"]
        )

    with right:

        st.metric(
            "Datasets Loaded",
            summary["datasets_loaded"]
        )

        st.metric(
            "Quality Score",
            f"{score}%"
        )