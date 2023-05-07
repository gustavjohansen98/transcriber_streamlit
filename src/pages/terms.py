import streamlit as st
from components import (
    terms_tab as terms,
    custom_styles as styles,
)

st.set_page_config(
    page_title="Transcribe | TERMS",
    page_icon="🎙️",
    initial_sidebar_state="collapsed",
    layout="centered",
)
styles.remove_all_top_level_styles()
terms.generate_terms_tab()
