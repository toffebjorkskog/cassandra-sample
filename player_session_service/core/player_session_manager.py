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
from .validation import validate_start_event, validate_end_event


def insert_player_events(player_events):
    if len(player_events) > 10:
        raise ValueError('Events must not be more than 10')
    if len(player_events) == 0:
        raise ValueError('Amount of events must be between 1 and 10')

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
    returndata = {'player_session': dict(player_session)}

    completed_session = check_event_completed(event)
    if completed_session is not None:
        returndata['completed_session'] = dict(completed_session)

    return returndata


def insert_end_event(event):
    validate_end_event(event)

    player_session = EndSessionEvents.create(
        player_id=uuid.UUID(event['player_id']),
        ts=dateutil.parser.parse(event['ts']),
        session_id=uuid.UUID(event['session_id']),
    )
    player_session.save()
    returndata = {'player_session': dict(player_session)}
    completed_session = check_event_completed(event)
    if completed_session is not None:
        returndata['completed_session'] = dict(completed_session)

    return returndata


def check_event_completed(event):
    '''
    Since we cannot be sure if the data arrives in chronological order,
    the sample json data can have end events before start events.
    Thus, we cannot just say that an order is completed once the end event
    arrives. Although, if that was the case, we would need fewer lookups.
    '''
    session_id = event['session_id']
    player_id = event['player_id']
    events = SessionEventsByPlayerId.objects(player_id=player_id,
                                             session_id=session_id)
    if len(events) == 2:  # these are ordered by timestamp desc
        end_event = events[0]
        start_event = events[1]
        completed_session = CompletedSessionsByPlayerId.create(
            player_id=player_id,
            end_ts=end_event.ts,
            start_ts=start_event.ts,
            session_id=session_id,
            country=start_event.country,
        )
        return completed_session
    else:
        return None


def get_session_starts_for_country(country_code, hours):
    """
    Returns the latest session starts for the specified countr in the last x hours
    """
    last_x_hours = lastHourDateTime = datetime.datetime.now() - datetime.timedelta(hours)
    q = SessionStartsByCountry.objects().filter(country=country_code)
    q = q.filter(start_ts > last_x_hours)
    start_events = q.get()
    return {'start_events': dict(player_session)}
