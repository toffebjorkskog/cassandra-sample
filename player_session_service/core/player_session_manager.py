from cassandra.cluster import Cluster
from ..models.session_start_by_country import SessionStartByCountry

cluster = Cluster()


class PlayerSessionManager(object):

    def insert_player_events(self, player_events):
        for event in player_events:
            if event["event"] == "start":
                self.insert_start_event(event)

    def insert_start_event(event):
        eventStart = SessionStartByCountry()
        eventStart.country = event["country"]
        eventStart.daybucket = event["ts"][:10]
        eventStart.player_id = event["player_id"]
        eventStart.session_id = event["session_id"]
        eventStart.save()
