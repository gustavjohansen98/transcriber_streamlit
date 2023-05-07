import streamlit as st

def generate_upload_tab():
    with st.form("upload_form"):
        uploaded_file = st.file_uploader(
            label="💾 **Upload din fil**", 
            key="uploaded_file",
            accept_multiple_files=False, 
            help="""
            `Format` Vi understøtter alle lydformater!
            `Sikkerhed` Din fil bliver enkrypteret når den sendes til vores server. Filen bliver slettet, så snart transskriberingen er færdig.
            """,
        )
        user_email = st.text_input(
            label="📧 **Indtast din emailadresse**", 
            key="user_email",
            value="", 
            placeholder="name@example.com", 
            help="""
            `Hvorfor` Vi sender dig en mail med et link til transkriberingen, når den er klar.
            `Sikkerhed` Vi gemmer din email i 7 dage, så du kan tilgå din transskribering. Efter 7 dage sletter vi din email.
            `Marketing` Ingen spam og marketing fra os.
            """,
        )
        apply_diarization = st.radio(
            label="🧮 **Del op efter hvem der snakker hvornår**",
            key="apply_diarization",
            options=[
                "Ja",
                "Nej, der er kun een speaker"
            ],
            index=0,
            horizontal=True,
            help="""
            `Hvad` Din transskribering deles op efter, hvor mange forskellige personer der taler, så du nemt kan se, hvem der snakker hvornår.
            `Sikkerhed` Vi kan ikke sætte navne på personerne, hvorfor de tildeles labels som *SPEAKER_00*, *SPEAKER_01*, etc. Du kan i vores redigeringsværktøj rette labels til, så de passer med virkeligheden.
            """,
        )
        upload_form_submitted = st.form_submit_button("Start transskribering", use_container_width=True, type="primary")