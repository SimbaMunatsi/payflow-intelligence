"""
Pipeline History Page.

Author: Simba Munatsi
Project: PayFlow Intelligence Platform
"""

import pandas as pd
import streamlit as st

from components.api import (
    get_pipeline_history,
)


def render():
    """
    Render the Pipeline History page.
    """

    st.header("📜 Pipeline History")

    st.caption(
        "Historical ingestion pipeline runs."
    )

    st.divider()

    history = get_pipeline_history()

    if not history:

        st.info(
            "No pipeline history available."
        )

        return

    df = pd.DataFrame(history)

    st.metric(
        "Total Records",
        len(df),
    )

    st.divider()

    st.dataframe(

        df,

        width="stretch",

        hide_index=True,

    )