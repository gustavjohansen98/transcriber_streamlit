import streamlit as st

def generate_faq_tab():
    with st.expander("🍪 Bruger I cookies?", expanded=True):
        st.write("Nope.")
    with st.expander("📧 Hvordan behandler I min email?", expanded=True):
        st.write("Blah blah blah")
    with st.expander("💾 Hvordan behandler I min lydfil?", expanded=True):
        st.write("Blah blah blah")
    with st.expander("💾 Hvilke formater accepterer I?", expanded=False):
        st.write("Blah blah blah")
    with st.expander("👾 Jeg har fundet en fejl, hvad kan jeg gøre?", expanded=False):
        st.write("Blah blah blah")
    with st.expander("🤖 Hvilke teknologier bruger I?", expanded=False):
        st.write("Blah blah blah")