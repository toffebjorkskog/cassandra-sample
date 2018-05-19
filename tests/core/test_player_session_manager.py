import pytest
from player_session_service.core.player_session_manager import (
    insert_start_event, insert_end_event
)
from player_session_service.models.session_events_by_player_id import (
    SessionEventsByPlayerId
)
from helpfunctions import (
    get_sample_start_event, get_sample_end_event, session_event_exists,
    session_start_event_exists, session_end_event_exists
)


def test_create_start_event__event_is_added_to_cassandra():
    event = get_sample_start_event()
    session_id = '00000001-2128-436b-a689-38c47a477118'
    event['session_id'] = session_id

    state_before = session_start_event_exists(session_id=session_id)
    insert_start_event(event)
    state_after = session_start_event_exists(session_id=session_id)

    assert state_before != state_after


def test_create_end_event__event_is_added_to_cassandra():
    session_id = '00000001-2128-436b-a689-38c47a477118'
    state_before = session_end_event_exists(session_id)

    event = get_sample_end_event()
    event['session_id'] = session_id
    insert_end_event(event)

    state_after = session_end_event_exists(session_id)
    assert state_before != state_after


def test_create_start_event__uuid_is_prettified():
    session_id = 'e0d836e6-2128-436b-a689-38c47a477118'

    event = get_sample_start_event()
    event['player_id'] = '02a0511372394597aa76c89f106aa547'
    returndata = insert_start_event(event)

    uuid_with_dashes = '02a05113-7239-4597-aa76-c89f106aa547'
    assert str(returndata['player_session']['player_id']) == uuid_with_dashes
