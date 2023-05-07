from components import (
    upload_tab as upload,
    example_tab as example,
    guide_tab as guide,
    faq_tab as faq,
    about_tab as about,
    terms_tab as terms
)
import streamlit as st
import utils     as utils

st.set_page_config(
    page_title="Transcribe | BETA",
    page_icon="🎙️",
    initial_sidebar_state="collapsed",
    layout="centered"
)

# st.markdown("""
# <style>
# #MainMenu {
#   visibility: hidden;
# }
# footer {
#   visibility: hidden;
# }
# header[data-testid="stHeader"] {
#   visibility: hidden;
# }
# .block-container {
#   padding-top: 2rem;
#   padding-right: 1rem;
#   padding-bottom: 2rem;
#   padding-left: 1rem;
# }
# </style>
# """, unsafe_allow_html=True)

# remove header, sidebar, burgerbar, streamlit footer, and padding in mainComponent
st.markdown("""
<style>
/*
#MainMenu {visibility: hidden;}
footer {visibility: hidden;} 
header[data-testid="stHeader"] {
  visibility: hidden;
}
*/
.block-container.css-1y4p8pa {
  padding: 2rem; 2rem; 2rem; 2rem;
  /* padding: 4rem; 0rem; 2rem; 0rem; */
}
</style>
""", unsafe_allow_html=True)
utils.hide_footer()
    
st.title('AI transskribering `BETA`')

st.markdown("""
> 🫶 **Gratis** </br>
> 🔒 **GDPR sikret** </br>
> 🚀 **1 time**s lyd på **~5 minutter** </br>
> 🔥 Delt op efter **hvem snakker hvornår**
""", unsafe_allow_html=True)

upload_tab, example_tab, guide_tab, faq_tab, about_tab, terms_tab = (
    st.tabs([
        "⚡ :orange[**UPLOAD**]", 
        "👀 **EKSEMPEL**", 
        "🎓 **GUIDE**", 
        "🤷 **F.A.Q.**", 
        "💜 **OM OS**", 
        "📄 **VILKÅR**"
    ])
)

with upload_tab:
    upload.generate_upload_tab()

with example_tab:
    example.generate_example_tab()
    
with guide_tab:
    guide.generate_guide_tab()

with faq_tab:
    faq.generate_faq_tab()

with about_tab:
    about.generate_about_tab()

with terms_tab:
    terms.generate_terms_tab()