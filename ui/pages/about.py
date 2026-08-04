"""
About Page.

Displays information about the PayFlow Intelligence Platform.

Author: Simba Munatsi
Project: PayFlow Intelligence Platform
"""

import streamlit as st


def render():
    """
    Render the About page.
    """

    st.header("ℹ About PayFlow Intelligence")

    st.caption(
        "Enterprise Payment Operations & Data Intelligence Platform"
    )

    st.divider()

    # =====================================================
    # Platform Overview
    # =====================================================

    st.subheader("🏢 Platform Overview")

    st.markdown(
        """
PayFlow Intelligence is an enterprise-grade data platform designed to
ingest, validate, transform and analyse payment operations data.

The platform enables payment operations teams to monitor data quality,
track pipeline execution, build an analytics warehouse and provide
actionable operational insights through an intuitive dashboard.
"""
    )

    st.divider()

    # =====================================================
    # Core Modules
    # =====================================================

    st.subheader("⚙ Core Modules")

    modules = [

        "Landing Layer",

        "Staging Layer",

        "Validation Engine",

        "Analytics Warehouse",

        "FastAPI Services",

        "Streamlit Dashboard",

        "AI Insights",

        "Reporting",

    ]

    for module in modules:

        st.success(module)

    st.divider()

    # =====================================================
    # Platform Features
    # =====================================================

    st.subheader("✨ Platform Features")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
- Automated data ingestion
- Data quality validation
- Referential integrity checks
- Business rule validation
- Analytics warehouse
- Pipeline monitoring
""")

    with col2:

        st.markdown("""
- Interactive dashboard
- Pipeline history
- Executive reporting
- Operational insights
- REST API
- Modular architecture
""")

    st.divider()

    # =====================================================
    # Technology Stack
    # =====================================================

    st.subheader("🛠 Technology Stack")

    st.markdown("""
- Python
- Pandas
- FastAPI
- Streamlit
- Parquet
- Pydantic
- Docker (Deployment)
""")

    st.divider()

    # =====================================================
    # Roadmap
    # =====================================================

    st.subheader("🚀 Future Roadmap")

    roadmap = [

        "Real-time payment monitoring",

        "Fraud detection",

        "Predictive settlement analytics",

        "Merchant risk scoring",

        "Automated anomaly detection",

        "Cloud deployment",

        "Machine learning forecasting",

        "Generative AI operational assistant",

    ]

    for item in roadmap:

        st.info(item)

    st.divider()

    # =====================================================
    # Project Statistics
    # =====================================================

    st.subheader("📊 Project Summary")

    stat1, stat2, stat3 = st.columns(3)

    with stat1:

        st.metric(
            "Pipeline Layers",
            4
        )

    with stat2:

        st.metric(
            "UI Pages",
            8
        )

    with stat3:

        st.metric(
            "API Services",
            2
        )

    st.divider()

    # =====================================================
    # Developer
    # =====================================================

    st.subheader("👨‍💻 Developer")

    st.markdown(
        """
**Simba Munatsi**

PayFlow Intelligence Platform

Enterprise Data Engineering Portfolio Project
"""
    )

    st.caption(
        "© 2026 PayFlow Intelligence Platform"
    )