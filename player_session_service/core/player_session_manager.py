from cassandra.cluster import Cluster
from ..models.session_start_by_country import SessionStartByCountry
import uuid
from .utils import get_datetime


def insert_player_events(player_events):
    for event in player_events:
        if event["event"] == "start":
            insert_start_event(event)


def insert_start_event(event):

    eventStart = SessionStartByCountry.create(
        country=event['country'],
        daybucket=event['ts'][:10],
        start_ts=get_datetime(event['ts']),
        #player_id=uuid.UUID(event['player_id'])
        #sess_id=uuid.UUID(event['session_id'])
    )
    eventStart.save()
