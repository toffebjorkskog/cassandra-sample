import pytest
from player_session_service.core.player_session_manager import (
    insert_start_event
)
from player_session_service.models.session_events_by_player_id import (
    SessionEventsByPlayerId
)
from helpfunctions import get_sample_start_event, get_sample_end_event


def test_create_start_event__event_is_added_to_cassandra():
    session_id = 'e0d836e6-2128-436b-a689-38c47a477118'
    try:
        q = SessionEventsByPlayerId.filter(session_id=session_id)
        events_before = q.get()
        length_before = events_before(events_before)
    except Exception:
        length_before = 0

    event = get_sample_start_event()
    event['session_id'] = session_id
    returndata = insert_start_event(event)
    q = SessionEventsByPlayerId.filter(session_id=session_id)
    events_after = q.get()

    assert len(events_after) != length_before


def test_create_start_event__uuid_is_prettified():
    event = get_sample_start_event()
    event['player_id'] = '02a0511372394597aa76c89f106aa547'
    returndata = insert_start_event(event)
    uuid_with_dashes = '02a05113-7239-4597-aa76-c89f106aa547'
    assert str(returndata['player_id']) == uuid_with_dashes
