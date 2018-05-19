import dateutil.parser

from player_session_service.models.session_events_by_player_id import (
    SessionEventsByPlayerId,
    StartSessionEvents,
    EndSessionEvents
)
from cassandra.cqlengine.query import DoesNotExist as _DoesNotExist


def get_sample_start_event():
    return {
        'event': 'start',
        'country': 'FI',
        'player_id': '0a2d12a1a7e145de8bae44c0c6e06629',
        'session_id': '4a0c43c9-c43a-42ff-ba55-67563dfa35d4',
        'ts': '2016-12-02T12:48:05.520022'
    }


def get_sample_end_event():
    return {
        'event': 'end',
        'player_id': '0a2d12a1a7e145de8bae44c0c6e06629',
        'session_id': '4a0c43c9-c43a-42ff-ba55-67563dfa35d4',
        'ts': '2016-12-02T12:49:05.520022'
    }


def session_event_exists(session_id):
    try:
        q = SessionEventsByPlayerId.get(session_id=session_id)
        events = q.get()
        return len(events) > 0
    except _DoesNotExist:
        return False
    else:
        return False


def session_start_event_exists(session_id):
    try:
        q = StartSessionEvents.get(session_id=session_id)
        events = q.get()
        return len(events) > 0
    except _DoesNotExist:
        return False
    else:
        return False


def session_end_event_exists(session_id):
    try:
        q = EndSessionEvents.get(session_id=session_id)
        events = q.get()
        return len(events) > 0
    except _DoesNotExist:
        return False
    else:
        return False
