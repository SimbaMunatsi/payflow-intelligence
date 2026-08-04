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
    "Enterprise Payment Operations & Data Quality Platform"
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

        st.success("🟢 API Connected")

    else:

        st.error("🔴 API Unavailable")

except Exception:

    st.error("🔴 Cannot connect to API")

st.divider()

# =====================================================
# Run Pipeline
# =====================================================

if st.button(
    "▶ Run Pipeline",
    use_container_width=True,
):

    with st.spinner("Running pipeline..."):

        response = requests.post(
            f"{API_URL}/pipeline/run",
            timeout=300,
        )

    if response.status_code == 200:

        result = response.json()

        # =====================================================
        # Extract Dashboard Sections
        # =====================================================

        kpis = result["kpis"]

        pipeline = result["pipeline"]

        quality = result["quality"]

        warehouse = result["warehouse"]

        summary = result["summary"]

        st.success(
            "Pipeline completed successfully."
        )

        # =====================================================
        # Executive Dashboard
        # =====================================================

        st.subheader("📈 Executive Dashboard")

        col1, col2, col3, col4 = st.columns(4)

        with col1:

            st.metric(
                "Quality Score",
                f"{kpis['quality_score']}%",
            )

        with col2:

            st.metric(
                "Rows Processed",
                f"{kpis['rows_processed']:,}",
            )

        with col3:

            st.metric(
                "Warehouse Tables",
                kpis["warehouse_tables"],
            )

        with col4:

            st.metric(
                "Execution Time",
                f"{kpis['execution_time']:.2f}s",
            )

        st.divider()

        # =====================================================
        # Pipeline Status
        # =====================================================

        st.subheader("⚙️ Pipeline Status")

        for stage in pipeline["stages"]:

            if stage["status"] == "Completed":

                st.success(
                    f"{stage['name']} ✓"
                )

            else:

                st.error(
                    f"{stage['name']} ✗"
                )

        st.divider()

        # =====================================================
        # Data Quality + Warehouse
        # =====================================================

        left, right = st.columns(2)

        # -----------------------------------------------------

        with left:

            st.subheader("📊 Data Quality Center")

            for category in quality["categories"]:

                st.metric(
                    category["name"],
                    f"{category['pass_rate']}%",
                )

                st.progress(
                    category["pass_rate"] / 100
                )

                st.caption(
                    f"✅ Passed: {category['passed']}    |    ❌ Failed: {category['failed']}"
                )

                st.write("")

        # -----------------------------------------------------

        with right:

            st.subheader("🏢 Warehouse Explorer")

            for table in warehouse["tables"]:

                icon = (
                    "📦"
                    if table["table_type"] == "Fact"
                    else "📁"
                )

                st.write(
                    f"{icon} **{table['name']}**"
                )

                st.caption(
                    f"{table['table_type']} • {table['rows']:,} rows"
                )

        st.divider()

        # =====================================================
        # Pipeline Summary
        # =====================================================

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

    else:

        st.error(
            "Pipeline execution failed."
        )

        try:

            st.json(
                response.json()
            )

        except Exception:

            st.text(
                response.text
            )