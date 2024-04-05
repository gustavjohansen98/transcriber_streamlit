import time
from streamlit.runtime.uploaded_file_manager import UploadedFile
from utils import utils
# from modal import Function
import modal


class InvalidEmailError(Exception):
    def __init__(self):
        self.message = "Invalid email"
        super().__init__(self.message)

class InvalidFileError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class ServerError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def spawn_pipeline(
    email: str, 
    file: UploadedFile = None, 
):
    if file is None:
        raise InvalidFileError("Vælg en fil")
    
    if not utils.validate_email(email):
        raise InvalidEmailError()

    try:    
        pipeline    = modal.Function.lookup(
            "transcriber-pipeline", 
            "start_transcribing",
        )

        audio_bytes       = file.read()
        user_session_id   = utils.get_session_id()
        user_ip_address   = utils.get_remote_ip()
        extension         = file.name.split('.')[-1]
        size              = file.size
        file_type         = file.type
        upload_time       = time.time_ns()

        modal_job = pipeline.spawn(
            user_id=email,
            transcription_id=user_session_id,
            storage_url="file",
            audio_bytes=audio_bytes,
            client_info={
                "user_session_id": user_session_id,
                "user_ip_address": user_ip_address,
                "extension": extension,
                "size": size,
                "file_type": file_type,
                "upload_time": upload_time,
            }
        )
        print(modal_job.object_id)
        return True

    except Exception as e:
        print(str(e))
        raise ServerError("Ups, der gik noget galt hos os - prøv igen om et øjeblik")

