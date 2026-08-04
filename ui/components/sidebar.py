"""
Sidebar Component.

Renders the application sidebar and
returns the selected page.

Author: Simba Munatsi
Project: PayFlow Intelligence Platform
"""

import streamlit as st

from components.api import get_health


def render_sidebar() -> str:
    """
    Render the application sidebar.

    Returns
    -------
    str
        Selected navigation page.
    """

    with st.sidebar:

        st.title("📊 PayFlow")

        st.caption(
            "Enterprise Intelligence Platform"
        )

        st.divider()

        page = st.radio(

            "Navigation",

            [

                "📊 Dashboard",

                "⚙ Pipeline",

                "📈 Data Quality",

                "🏢 Warehouse",

                "📜 History",

                "📄 Reports",

                "🤖 AI Insights",

                "ℹ About",

            ],

        )

        st.divider()

        # ==========================================
        # API Status
        # ==========================================

        st.subheader("System Status")

        if get_health():

            st.success(
                "🟢 API Online"
            )

        else:

            st.error(
                "🔴 API Offline"
            )

        st.divider()

        # ==========================================
        # Platform Information
        # ==========================================

        st.markdown("### Platform")

        st.caption(
            "Version 1.0"
        )

        st.caption(
            "Environment: Development"
        )

        st.caption(
            "PayFlow Intelligence"
        )

        st.divider()

        st.caption(
            "© 2026 Simba Munatsi"
        )

    return page