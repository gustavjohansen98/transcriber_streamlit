from streamlit.runtime.uploaded_file_manager import UploadedFile
from streamlit.logger import get_logger
from utils import utils
from modal import Function


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
    logger = get_logger(__name__)

    if file is None:
        raise InvalidFileError("Vælg en fil")
    
    if not utils.validate_email(email):
        raise InvalidEmailError()

    log_file = " ".join([
        f"[UPLOAD]",
        f"(TYPE: {file.type})",
        f"(NAME: {file.name.split('.')[-1]})",
        f"(SIZE: {file.size})",
    ])
    logger.info(log_file)

    try:    
        pipeline    = Function.lookup(
            "transcriber-pipeline", 
            "start_transcribing",
        )
        audio_bytes = file.read()
        job         = pipeline.spawn(
            user_id=email,
            transcription_id="",
            storage_url="file",
            audio_bytes=audio_bytes,
        )

        logger.info(f"[PIPELINE] (JOB_ID: {job.object_id})")
        return True

    except Exception as e:
        logger.exception(e)
        raise ServerError("Ups, der gik noget galt hos os - prøv igen om et øjeblik")

