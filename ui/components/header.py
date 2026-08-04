"""
Header Component.

Renders the application header used by all pages.

Author: Simba Munatsi
Project: PayFlow Intelligence Platform
"""

from datetime import datetime

import streamlit as st


def render_header():
    """
    Render the application header.
    """

    col1, col2 = st.columns([4, 1])

    with col1:

        st.title(
            "📊 PayFlow Intelligence Platform"
        )

        st.caption(
            "Enterprise Payment Operations & Data Quality Dashboard"
        )

    with col2:

        st.metric(
            "Status",
            "🟢 Online",
        )

        st.caption(
            datetime.now().strftime(
                "%d %b %Y %H:%M"
            )
        )

    st.divider()