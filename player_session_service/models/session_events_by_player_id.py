from player_session_service.models import db


class SessionEventsByPlayerId(db.Model):
    '''
    Model for storing the a session event of a gamer ordered by end time
    '''
    __table_name_case_sensitive__ = 'session_events_by_player_id'
    __default_ttl__ = 31536000
    session_id = db.columns.UUID(partition_key=True, primary_key=True)
    ts = db.columns.DateTime(primary_key=True, clustering_order='DESC')
    player_id = db.columns.UUID(primary_key=True)
    event = db.columns.Text(primary_key=True, discriminator_column=True)
    country = db.columns.Text(required=True)


class StartSessionEvents(SessionEventsByPlayerId):
    __discriminator_value__ = 'start'


class EndSessionEvents(SessionEventsByPlayerId):
    __discriminator_value__ = 'end'
