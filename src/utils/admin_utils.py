from streamlit.runtime.runtime import Runtime
from streamlit.runtime.session_manager import SessionInfo, ActiveSessionInfo

def get_live_stats():
    runtime       = Runtime.instance()
    runtime_state = runtime.state

    print("\n########\n")
    print("runtime_state.name")
    print(runtime_state.name)
    print("\n####\n")

    print("Current amount of active sessions:")
    print("\t", runtime._session_mgr.num_active_sessions())
    print("Sessions:")
    for session in runtime._session_mgr.list_sessions():
        print(f"\tSESSION_ID: {session.session.id}")
        if type(session) is not ActiveSessionInfo:
            print(f"\tIS_ACTIVE: {session.is_active()}")
        else:
            print(f"\tIS_ACTIVE: True")
        print(f"\tSCRIPT_RUN_COUNT: {session.script_run_count}")
        print("\n")
    print("\n####\n")