"""
PayFlow Intelligence Platform.

Application entry point.

Author: Simba Munatsi
Project: PayFlow Intelligence Platform
"""

import streamlit as st

from components.header import render_header
from components.sidebar import render_sidebar

from views import dashboard
from views import pipeline
from views import quality
from views import warehouse
from views import history
from views import reports
from views import ai
from views import about

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

elif page == "🤖 AI_Insights":

    ai.render()

elif page == "ℹ About":

    about.render()