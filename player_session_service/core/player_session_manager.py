from cassandra.cluster import Cluster
from ..models.session_starts_by_country import SessionStartsByCountry
from ..models.completed_sessions_by_player_id import (
    CompletedSessionsByPlayerId
)
from ..models.session_events_by_player_id import (
    StartSessionEvents, EndSessionEvents, SessionEventsByPlayerId
)
import uuid
import dateutil.parser
from .validation import validate_start_event


def insert_player_events(player_events):
    for event in player_events:
        if event['event'] == 'start':
            insert_start_event(event)
        else:
            insert_end_event(event)


def insert_start_event(event):
    validate_start_event(event)
    event_start = SessionStartsByCountry.create(
        country=event['country'],
        daybucket=event['ts'][:10],
        start_ts=dateutil.parser.parse(event['ts']),
        player_id=uuid.UUID(event['player_id']),
        session_id=uuid.UUID(event['session_id'])
    )
    event_start.save()

    player_session = StartSessionEvents.create(
        player_id=uuid.UUID(event['player_id']),
        country=event['country'],
        ts=dateutil.parser.parse(event['ts']),
        session_id=uuid.UUID(event['session_id']),
    )
    player_session.save()
    check_event_completed(event)
    return dict(event_start)


def insert_end_event(event):
    validate_end_event(event)

    player_session = PlayerSessionsByPlayerId.create(
        player_id=uuid.UUID(event['player_id']),
        end_ts=dateutil.parser.parse(event['ts']),
        session_id=uuid.UUID(event['session_id']),
    )
    player_session.save()

    player_session = EndSessionEvents.create(
        player_id=uuid.UUID(event['player_id']),
        ts=dateutil.parser.parse(event['ts']),
        session_id=uuid.UUID(event['session_id']),
    )
    check_event_completed(event)

    return dict(eventStart)


def check_event_completed(event):
    '''
    Since we cannot be sure if the data arrives in chronological order,
    we cannot just say that an order is completed once the end event arrives.
    Although, if that was the case, we would need fewer lookups.
    '''
    q = SessionEventsByPlayerId.filter(session_id=event['session_id'])
    events = q.get()
    if len(events) == 2:  # these are ordered by timestamp desc
        end_event = events[0]
        start_event = events[1]
        completed_session = CompletedSessionsByPlayerId.create(
            player_id=start_event.player_id,
            start_ts=start_event.ts,
            end_ts=end_event.ts,
            session_id=start_event.session_id,
            country=start_event.country,
        )
        return True
    else:
        return False
