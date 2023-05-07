import server_api
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
            
        upload_form_submitted = st.form_submit_button("Start transskribering", use_container_width=True, type="primary")

        if upload_form_submitted:
            try:
                with st.spinner("Tjekker fil ..."):
                    success = server_api.spawn_pipeline(
                        email=user_email,
                        file=uploaded_file,
                    )
                if success:
                    st.success(
                        f"Yay! Vi sender resultatet til **{user_email}** inden længe (husk evt. at tjekke spam)",
                        icon="🥳"
                    )
                    st.balloons()
            except server_api.InvalidEmailError as e:
                st.error(str(e))
            except server_api.InvalidFileError as e:
                st.error(str(e))
            except server_api.ServerError as e:
                st.error(str(e))
                
