"""
Dashboard Page.

Enterprise dashboard for the PayFlow
Intelligence Platform.

Author: Simba Munatsi
Project: PayFlow Intelligence Platform
"""

import streamlit as st

from components.api import get_dashboard, run_pipeline


def render():
    """
    Render the Dashboard page.
    """

    st.subheader("📊 Executive Dashboard")

    st.subheader("📅 Analysis Period")

    col1, col2 = st.columns(2)

    with col1:

        start_date = st.date_input(
            "Start Date"
        )

    with col2:

        end_date = st.date_input(
            "End Date"
        )

    st.divider()

    if st.button(
        "▶ Run Pipeline",
        width='stretch',
    ):

        with st.spinner(
            "Running pipeline..."
        ):

            result = get_dashboard(
                start_date=start_date,
                end_date=end_date
            )

        render_dashboard(result)


# =====================================================
# Main Dashboard
# =====================================================

def render_dashboard(result: dict, start_date=None, end_date=None):
    """
    Render the complete dashboard.
    """

    kpis = result["kpis"]

    pipeline = result["pipeline"]

    quality = result["quality"]

    warehouse = result["warehouse"]

    summary = result["summary"]

    st.success(
        "Pipeline completed successfully."
    )

    # st.info(

    #     f"Showing results from "

    #     f"**{start_date}** "

    #     f"to "

    #     f"**{end_date}**"

    # )

    executive = result["executive"]

    render_executive_kpis(
        executive["kpis"]
    )

    render_business_charts(
        executive["charts"]
    )

    render_kpis(kpis)

    render_pipeline_status(pipeline)

    render_quality_and_warehouse(
        quality,
        warehouse,
    )

    render_summary(
        result,
        kpis,
        summary,
    )


# =====================================================
# Executive KPI Cards
# =====================================================

def render_executive_kpis(kpis):

    st.subheader(
        "🏦 Executive Operations Overview"
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "Transactions",
            f"{kpis['total_transactions']:,}"
        )

    with col2:

        st.metric(
            "Success Rate",
            f"{kpis['success_rate']:.2f}%"
        )

    with col3:

        st.metric(
            "Settlement Rate",
            f"{kpis['settlement_rate']:.2f}%"
        )

    with col4:

        st.metric(
            "Open Tickets",
            kpis["open_support_tickets"]
        )

    st.divider()

# =====================================================
# Business Charts
# =====================================================

import pandas as pd


def render_business_charts(charts):

    st.subheader(
        "📊 Business Intelligence"
    )

    for chart in charts:

        st.markdown(
            f"#### {chart['title']}"
        )

        df = pd.DataFrame(

            {

                "Category":
                    chart["labels"],

                "Value":
                    chart["values"],

            }

        )

        if chart["chart_type"] == "pie":

            st.bar_chart(

                df,

                x="Category",

                y="Value",

                width="stretch",

            )

        else:

            st.bar_chart(

                df,

                x="Category",

                y="Value",

                width="stretch",

            )

        st.write("")

    st.divider()    

# =====================================================
# KPI Section
# =====================================================

def render_kpis(kpis):

    st.subheader("🖥️ System Health")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "Quality Score",
            f"{kpis['quality_score']}%"
        )

    with col2:

        st.metric(
            "Rows Processed",
            f"{kpis['rows_processed']:,}"
        )

    with col3:

        st.metric(
            "Warehouse Tables",
            kpis["warehouse_tables"]
        )

    with col4:

        st.metric(
            "Execution Time",
            f"{kpis['execution_time']:.2f}s"
        )

    st.divider()


# =====================================================
# Pipeline Status
# =====================================================

def render_pipeline_status(pipeline):

    st.subheader("⚙ Pipeline Status")

    cols = st.columns(
        len(pipeline["stages"])
    )

    for col, stage in zip(
        cols,
        pipeline["stages"],
    ):

        with col:

            st.success(
                stage["name"]
            )

            st.caption(
                stage["status"]
            )

    st.divider()


# =====================================================
# Quality + Warehouse
# =====================================================

def render_quality_and_warehouse(
    quality,
    warehouse,
):

    left, right = st.columns(2)

    # =============================================

    with left:

        st.subheader(
            "📊 Data Quality Center"
        )

        for category in quality[
            "categories"
        ]:

            st.metric(

                category["name"],

                f"{category['pass_rate']}%",

            )

            st.progress(
                category["pass_rate"] / 100
            )

            st.caption(

                f"✅ Passed: {category['passed']}"

            )

            st.caption(

                f"❌ Failed: {category['failed']}"

            )

            st.write("")

    # =============================================

    with right:

        st.subheader(
            "🏢 Warehouse Explorer"
        )

        for table in warehouse[
            "tables"
        ]:

            icon = (

                "📦"

                if table["table_type"] == "Fact"

                else "📁"

            )

            st.write(

                f"{icon} **{table['name']}**"

            )

            st.caption(

                f"{table['table_type']}"

            )

            st.caption(

                f"{table['rows']:,} rows"

            )

            st.write("")


# =====================================================
# Summary
# =====================================================

def render_summary(
    result,
    kpis,
    summary,
):

    st.divider()

    st.subheader(
        "📋 Pipeline Execution Summary"
    )

    left, right = st.columns(2)

    with left:

        st.markdown(f"""
**Run Status**

{result["status"].upper()}

**Datasets Loaded**

{summary["datasets_loaded"]}

**Validation Rules**

{summary["validation_rules"]}

**Execution Time**

{kpis["execution_time"]:.2f} seconds
""")

    with right:

        st.markdown(f"""
**Rules Passed**

{summary["rules_passed"]}

**Rules Failed**

{summary["rules_failed"]}

**Quality Score**

{kpis["quality_score"]}%

**Warehouse Tables**

{kpis["warehouse_tables"]}

**Run Timestamp**

{summary["run_timestamp"]}
""")