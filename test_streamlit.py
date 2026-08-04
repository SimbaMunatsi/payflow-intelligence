import streamlit as st

from ui.components.sidebar import render_sidebar

page = render_sidebar()

st.write(page)