import api.server_api as server_api
import streamlit as st


def generate_upload_tab():
    with st.form("upload_form"):

        uploaded_file = st.file_uploader(
            label="💾 **Upload din fil**", 
            key="uploaded_file",
            accept_multiple_files=False,
            type=['mp3', 'mp4', 'wav', 'm4a', 'flac', 'acc', 'wma'],
            help="""
            `Format` 
            Vi understøtter pt. *mp3*, *mp4*, *wav*, *m4a*, *flac*, *acc*, *wma*.

            `Sikkerhed` 
            Din fil bliver enkrypteret, når den sendes til vores server. Filen bliver slettet, så snart transskriberingen er færdig.
            """,
        )
        
        user_email = st.text_input(
            label="📧 **Indtast din emailadresse**", 
            key="user_email",
            value="", 
            placeholder="hello@world.com", 
            help="""
            `Hvorfor` 
            Vi sender dig en mail med et link til transskriberingen, når den er klar.

            `Sikkerhed` 
            Din email bliver slettet, så snart vi har sendt resultatet til dig.

            `Marketing` 
            Ingen spam og marketing fra os.
            """,
        )

        accepted_terms = st.checkbox(
            label='Jeg har læst og accepteret [betingelser](/terms)',
            key="accept_terms",
            value=False,
        )
            
        upload_form_submitted = st.form_submit_button(
            label="Start transskribering",
            use_container_width=True,
            type="primary",
        )

        if upload_form_submitted:
            if uploaded_file is None and len(user_email) == 0:
                st.warning("Udfyld felterne og accepter betingelser for at gå videre")
                return

            if not accepted_terms:
                st.error("Accepter betingelser for at gå videre")
                return

            try:
                with st.spinner("Tjekker fil ..."):
                    success = server_api.spawn_pipeline(
                        email=user_email,
                        file=uploaded_file,
                    )

                if success:
                    st.success(
                        f"Yay! Vi sender din transskribering til **{user_email}** inden længe (husk evt. at tjekke din spam mappe)",
                        icon="🥳"
                    )
                    st.balloons()

            except server_api.InvalidEmailError as e:
                st.error(str(e))
            except server_api.InvalidFileError as e:
                st.error(str(e))
            except server_api.ServerError as e:
                st.error(str(e))
                
