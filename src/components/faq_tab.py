import streamlit as st

def generate_faq_tab():
    with st.expander("🍪 Bruger I cookies?", expanded=True):
        st.write("Nope. Ingen tracking eller lignende.")
    with st.expander("📧 Hvordan behandler I min email?", expanded=True):
        st.write("Vi opbevarer midlertidigt din email på vores server, indtil vi har sendt resultatet til dig. Derefter bliver den slettet.")
    with st.expander("💾 Hvordan behandler I min lydfil?", expanded=True):
        st.write("Når vores server modtager din lydfil, konverteres den til et format, som vores AI modeller kan forstå, og den originale fil slettes. Så snart modellerne er færdige med at processere den konverterede fil, bliver denne også slettet. <br><br> Din fil bliver selvfølgelig enkrypteret, før den sendes afsted.", unsafe_allow_html=True)
    with st.expander("💾 Hvilke formater accepterer I?", expanded=False):
        st.write("Vi accepterer pt. *mp3*, *mp4*, *wav*, *m4a*, *flac*, *acc*, *wma*. Skriv gerne en mail til **norsekode@norsekode.com**, hvis du har ønsker til flere formater!")
    with st.expander("👾 Jeg har fundet en fejl, hvad kan jeg gøre?", expanded=False):
        st.write("Skriv en mail til **norsekode@norsekode.com**")
    # with st.expander("🤖 Hvilke teknologier bruger I?", expanded=False):
    #     st.write("Blah blah blah")