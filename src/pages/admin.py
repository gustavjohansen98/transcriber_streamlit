import streamlit as st
from components import (
    terms_tab as terms,
    custom_styles as styles,
)

st.set_page_config(
    page_title="Transcribe | ADMIN",
    page_icon="🎙️",
    initial_sidebar_state="expanded",
    layout="wide",
)
styles.remove_all_top_level_styles()
terms.generate_terms_tab()
