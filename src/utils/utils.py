import re


def validate_email(email):
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
    # timezone = get_user_timezone()
    timezone = "Europe/Copenhagen"
    continent, city = timezone.split("/")
    return city, continent
