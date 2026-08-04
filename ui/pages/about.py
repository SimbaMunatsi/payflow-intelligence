"""
About Page.
"""

import streamlit as st


def render():

    st.header("ℹ About")

    st.markdown(
        """
### PayFlow Intelligence Platform

Enterprise payment operations platform for
monitoring, validating and analysing payment
data pipelines.

---

**Developer**

Simba Munatsi

---

**Core Capabilities**

- Data Ingestion
- Data Validation
- Analytics Warehouse
- FastAPI Services
- Streamlit Operations Dashboard
- AI-powered Payment Intelligence
"""
    )