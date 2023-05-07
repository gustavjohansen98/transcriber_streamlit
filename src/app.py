from utils import utils
from components import (
    upload_tab as upload,
    guide_tab as guide,
    faq_tab as faq,
    about_tab as about,
    terms_tab as terms,
    custom_styles as styles,
)
import streamlit as st


def main():
    st.set_page_config(
        page_title="Transcribe | BETA",
        page_icon="🎙️",
        layout="centered",
        initial_sidebar_state="collapsed",
    )
    styles.remove_all_top_level_styles()
    
    st.title('AI transskribering `BETA`')
    st.markdown("""
    > 🫶 **Gratis** </br>
    > 🔒 **GDPR sikret** </br>
    > 🚀 **1 time**s lyd på **~5 minutter** </br>
    > 🔥 Delt op efter **hvem snakker hvornår**
    """, unsafe_allow_html=True)

    upload_tab, guide_tab, faq_tab, about_tab, terms_tab = (
        st.tabs([
            "⚡ :orange[**UPLOAD**]", 
            "🎓 **GUIDE**", 
            "🤷 **F.A.Q.**", 
            "💜 **OM OS**", 
            "📄 **VILKÅR**"
        ])
    )

    with upload_tab:
        upload.generate_upload_tab()        
    with guide_tab:
        guide.generate_guide_tab()
    with faq_tab:
        faq.generate_faq_tab()
    with about_tab:
        about.generate_about_tab()
    with terms_tab:
        terms.generate_terms_tab()


if __name__ == "__main__":
    main()
