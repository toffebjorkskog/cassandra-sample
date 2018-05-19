import dateutil.parser

from player_session_service.models.session_events_by_player_id import (
    SessionEventsByPlayerId,
    StartSessionEvents,
    EndSessionEvents
)
from player_session_service.models.completed_sessions_by_player_id import (
    CompletedSessionsByPlayerId
)
from cassandra.cqlengine.query import DoesNotExist as _DoesNotExist


def get_sample_start_event(
    country='FI',
    player_id='0a2d12a1a7e145de8bae44c0c6e06629',
    session_id='4a0c43c9-c43a-42ff-ba55-67563dfa35d4',
    ts='2016-12-02T12:48:05.520022'
):
    '''
    Function to give you a sample start event.
    You can override default values in the parameters.
    '''
    return {
        'event': 'start',
        'country': country,
        'player_id': player_id,
        'session_id': session_id,
        'ts': ts
    }


def get_sample_end_event(
    country='FI',
    player_id='0a2d12a1a7e145de8bae44c0c6e06629',
    session_id='4a0c43c9-c43a-42ff-ba55-67563dfa35d4',
    ts='2016-12-02T13:33:09'
):
    '''
    Function to give you a sample end event.
    You can override default values in the parameters.
    '''
    return {
        'event': 'end',
        'country': country,
        'player_id': player_id,
        'session_id': session_id,
        'ts': ts
    }


def session_event_exists(player_id, session_id):
    try:
        q = SessionEventsByPlayerId.objects(player_id=player_id, session_id=session_id)
        events = q.get()
        return len(events) > 0
    except _DoesNotExist:
        return False
    else:
        return False


def session_start_event_exists(player_id, session_id):
    try:
        q = StartSessionEvents.objects(player_id=player_id,
                                       session_id=session_id)
        events = q.get()
        return len(events) > 0
    except _DoesNotExist:
        return False
    else:
        return False


def session_end_event_exists(player_id, session_id):
    try:
        q = EndSessionEvents.objects(player_id=player_id,
                                     session_id=session_id)
        events = q.get()
        return len(events) > 0
    except _DoesNotExist:
        return False
    else:
        return False


def completed_session_exists(player_id, session_id):
    try:
        q = CompletedSessionsByPlayerId.objects(player_id=player_id,
                                                session_id=session_id)
        events = q.get()
        return len(events) > 0
    except _DoesNotExist:
        return False
    else:
        return False
