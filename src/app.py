from components import (
    upload_tab as upload,
    guide_tab as guide,
    faq_tab as faq,
    about_tab as about,
    terms_tab as terms
)

import streamlit as st
import utils     as utils


def main():
    st.set_page_config(
        page_title="Transcribe | BETA",
        page_icon="🎙️",
        initial_sidebar_state="collapsed",
        layout="centered"
    )

    st.markdown("""
    <style>
    #MainMenu {
    visibility: hidden;
    }
    footer {
    visibility: hidden;
    }
    
    header[data-testid="stHeader"] {
    visibility: hidden;
    }
    
    .block-container {
    padding-top: 2rem;
    padding-right: 1rem;
    padding-bottom: 2rem;
    padding-left: 1rem;
    }
    </style>
    """, unsafe_allow_html=True)

    
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
    # app_logger = logging.getLogger("app_logger")
    main()
