import re
import json
import uuid

from streamlit_javascript import st_javascript
from streamlit import runtime
from streamlit.web.server.server import Server
from streamlit.runtime.runtime import Runtime
from streamlit.runtime.session_manager import SessionInfo, ActiveSessionInfo
from streamlit.runtime.scriptrunner.script_run_context import get_script_run_ctx
    

def init_session() -> tuple:
    city, continent = get_city_continent()
    _ctx = get_script_run_ctx()
    _session_dict = _ctx.__dict__
    print(_session_dict)
    print(city)
    print(continent)
    return city, continent, _session_dict

def get_session() -> dict[str, str]:
    _ctx = get_script_run_ctx()
    if _ctx is None:
        return None
 
    _session_dict = _ctx.__dict__
    print(_session_dict)   
    _id = _ctx.session_id
    _city, _continent = get_city_continent()
    _remote_ip = get_remote_ip()

    return {
        "_id": _id,
        "_ip": _remote_ip,
        "_city": _city,
        "_continent": _continent
    }

def get_session_id() -> str:
    _ctx = get_script_run_ctx()
    if _ctx is None: return None
    return _ctx.session_id


def get_remote_ip() -> str:
    try:
        _ctx = get_script_run_ctx()
        if _ctx is None: return None
        session_info = runtime.get_instance().get_client(_ctx.session_id)
        if session_info is None: return None
    except Exception as e:
        return None
    
    return session_info.request.remote_ip


def validate_email(email) -> bool:
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


def get_city_continent() -> tuple:
    default_tz = "Etc/UTC"
    # js_key = uuid.uuid4()
    timezone = st_javascript("""await (async () => {
            const userTimezone = Intl.DateTimeFormat().resolvedOptions().timeZone
            console.log(userTimezone)
            return userTimezone
        })().then(returnValue => returnValue)""")
    if timezone == 0:  # st_javascript returns 0 for null/undefined
        timezone = default_tz

    continent, city = timezone.split("/")
    return city, continent
