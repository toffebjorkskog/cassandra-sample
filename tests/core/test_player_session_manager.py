import pytest


def test_create_start_event():
    from player_session_service.core.player_session_manager import insert_start_event
    event = {
                "player_id": "02a0511372394597aa76c89f106aa547",
                "country": "AE",
                "event": "start",
                "session_id": "e0d836e6-2128-436b-a689-38c47a477118",
                "ts": "2016-11-06T03:11:56"
            }
    returndata = insert_start_event(event)
    assert str(returndata["player_id"]) == '02a05113-7239-4597-aa76-c89f106aa547'


def test_create_start_event_with_wrong_date():
    from player_session_service.core.player_session_manager import insert_start_event
    event = {
                "player_id": "02a0511372394597aa76c89f106aa547",
                "country": "AE",
                "event": "start",
                "session_id": "e0d836e6-2128-436b-a689-38c47a477118",
                "ts": "2016-99-06T03:11:56"
            }
    with pytest.raises(Exception) as e_info:
        returndata = insert_start_event(event)


def test_create_start_event_with_wrong_event_name():
    from player_session_service.core.player_session_manager import insert_start_event
    event = {
                "player_id": "02a0511372394597aa76c89f106aa547",
                "country": "AE",
                "event": "begin",
                "session_id": "e0d836e6-2128-436b-a689-38c47a477118",
                "ts": "2016-11-06T03:11:56"
            }

    with pytest.raises(ValueError) as e_info:
        returndata = insert_start_event(event)
