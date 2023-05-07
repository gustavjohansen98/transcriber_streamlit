from modal import Function

pipeline = Function.lookup("client-test", "streamlit_test")

def spawn_pipeline(
    email: str, 
    file: bytes = None,
):
    print("\n\nCalled spawner\n")
    pipeline_result = pipeline.call(echo_me=email)
    print(pipeline_result)