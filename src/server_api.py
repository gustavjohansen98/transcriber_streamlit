from streamlit.runtime.uploaded_file_manager import UploadedFile
from modal import Function

import utils

# pipeline = Function.lookup("client-test", "streamlit_test")

class InvalidEmailError(Exception):
    def __init__(self):
        self.message = "Invalid email"
        super().__init__(self.message)

class InvalidFileError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def spawn_pipeline(
    email: str, 
    file: UploadedFile = None, 
):
    if file is None:
        raise InvalidFileError(message="Vælg en fil")
    
    if not utils.validate_email(email):
        raise InvalidEmailError()
    
    return True
        
    