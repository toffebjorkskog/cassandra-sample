from datetime import datetime


def get_datetime(str):
    return datetime.strptime(str, str)


def get_timeformat(str):
    if len(str) == 26:
        return "%Y-%m-%dT%H:%M:%S.%f"
    else:
        return "%Y-%m-%dT%H:%M:%S"
