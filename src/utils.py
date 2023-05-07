import re
import streamlit as st
from markdownlit import mdlit

__hide_footer = """
<style>
footer {visibility: hidden;}
</style>
"""

__hide_burgerbar = """
<style>
#MainMenu {visibility: hidden;}
</style>
"""

__hide_header = """
<style>
header[data-testid="stHeader"] {
  background-color: red;
  // visibility: hidden;
  height: 0px;
}
</style>
"""

__remove_main_padding = """
<style>
.block-container.css-1y4p8pa {
  padding: 1rem; 1rem; 1rem;
}
</style>
"""

__small_divider = """
<hr style="margin-top: 0px; margin-bottom: 5px;" /> 
"""

def validate_email(email):
    """
    Takes a string and uses regex to validate that it is an email address.
    Returns True if the email address is valid, False otherwise.
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'    
    match = re.match(pattern, email)
    return bool(match)


def format_seconds_to_str(seconds: float):
    milliseconds = int(seconds*1000)
    seconds = int((milliseconds / 1000) % 60)
    minutes = int((milliseconds / (1000 * 60)) % 60)
    hours = int((milliseconds / (1000 * 60 * 60)) % 24)
    timestamp_text = ""
    if hours > 0:
        timestamp_text += f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    else:
        timestamp_text += f"{hours:02d}:"
        timestamp_text += f"{minutes:02d}:{seconds:02d}"
    return timestamp_text

def get_city_continent(log_result: bool = True) -> tuple:
    # timezone = get_user_timezone()
    timezone = "Europe/Copenhagen"
    continent, city = timezone.split("/")
    if log_result:
        log_string = "\n".join([
            f"\t[USER TIMEZONE]:",
            f"\t\tcity      -> {city}",
            f"\t\tcontinent -> {continent}",
        ])
        print(f"User is from")
    return city, continent

def hide_footer():
    st.markdown(__hide_footer, unsafe_allow_html=True)

def hide_burgerbar():
    st.markdown(__hide_burgerbar, unsafe_allow_html=True)

def hide_header():
    st.markdown(__hide_header, unsafe_allow_html=True)

def remove_main_padding():
    st.markdown(__remove_main_padding, unsafe_allow_html=True)

def small_divider():
    st.markdown(__small_divider, unsafe_allow_html=True)

def custom_divider(margin_top: int, margin_bottom: int):
    mdlit(
f"""
<hr style="margin-top: {margin_top}px; margin-bottom: {margin_bottom}px;" />
"""
    )

def indent(level: int = 1):
    return "&nbsp;" * level

def animate_balloons():
    st.balloons()
