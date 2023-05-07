import streamlit as st


def small_divider():
    __small_divider = """
    <hr style="margin-top: 0px; margin-bottom: 5px;" /> 
    """
    st.markdown(__small_divider, unsafe_allow_html=True)


def custom_divider(margin_top: int, margin_bottom: int):
    __divider = f"""
    <hr style="margin-top: {margin_top}px; margin-bottom: {margin_bottom}px;" />
    """
    st.markdown(__divider, unsafe_allow_html=True)


def remove_all_top_level_styles():
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

    div[data-testid="collapsedControl"] {
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


def indent(level: int = 1):
    return "&nbsp;" * level


def hide_footer():
    __hide_footer = """
    <style>
        footer {visibility: hidden;}
    </style>
    """
    st.markdown(__hide_footer, unsafe_allow_html=True)


def hide_burgerbar():
    __hide_burgerbar = """
    <style>
        #MainMenu {visibility: hidden;}
    </style>
    """
    st.markdown(__hide_burgerbar, unsafe_allow_html=True)


def hide_header():
    __hide_header = """
    <style>
    header[data-testid="stHeader"] {
        visibility: hidden;
    }
    </style>
    """
    st.markdown(__hide_header, unsafe_allow_html=True)


def remove_main_padding():
    __remove_main_padding = """
    <style>
    .block-container {
        padding-top: 2rem;
        padding-right: 1rem;
        padding-bottom: 2rem;
        padding-left: 1rem;
    }
    </style>
    """
    st.markdown(__remove_main_padding, unsafe_allow_html=True)
