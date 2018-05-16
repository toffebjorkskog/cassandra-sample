from cassandra.cluster import Cluster
from ..models.session_start_by_country import SessionStartByCountry


def insert_player_events(player_events):
    for event in player_events:
        if event["event"] == "start":
            insert_start_event(event)


def insert_start_event(event):
    eventStart = SessionStartByCountry.create(
        country=event["country"],
        daybucket=event["ts"][:10],
        start_ts=event["ts"],
        player_id=event["player_id"],
        session_id=event["session_id"]
    )
    eventStart.save()
