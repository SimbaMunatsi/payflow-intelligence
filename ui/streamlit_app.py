"""
PayFlow Intelligence Platform.

Application entry point.

Author: Simba Munatsi
Project: PayFlow Intelligence Platform
"""

import streamlit as st

from components.header import render_header
from components.sidebar import render_sidebar

from pages import dashboard
from pages import pipeline
from pages import quality
from pages import warehouse
from pages import history
from pages import reports
from pages import ai
from pages import about

# =====================================================
# Streamlit Configuration
# =====================================================

st.set_page_config(

    page_title="PayFlow Intelligence",

    page_icon="📊",

    layout="wide",

    initial_sidebar_state="expanded",

)

# =====================================================
# Layout
# =====================================================

render_header()

page = render_sidebar()

# =====================================================
# Routing
# =====================================================

if page == "📊 Dashboard":

    dashboard.render()

elif page == "⚙ Pipeline":

    pipeline.render()

elif page == "📈 Data Quality":

    quality.render()

elif page == "🏢 Warehouse":

    warehouse.render()

elif page == "📜 History":

    history.render()

elif page == "📄 Reports":

    reports.render()

elif page == "🤖 AI Insights":

    ai.render()

elif page == "ℹ About":

    about.render()