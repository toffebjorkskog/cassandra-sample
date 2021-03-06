from app.models import db


class CompletedSessionsByPlayerId(db.Model):
    '''
    Model for storing the completed sessions of a gamer ordered by end time
    '''
    __table_name_case_sensitive__ = 'completed_sessions_by_player_id'
    __default_ttl__ = 31536000
    player_id = db.columns.UUID(partition_key=True, primary_key=True)
    session_id = db.columns.UUID(primary_key=True)
    end_ts = db.columns.DateTime(primary_key=True, clustering_order='DESC')
    country = db.columns.Text(required=True)
    start_ts = db.columns.DateTime()

    def get_data(self):
        return {
            'type': 'completed',
            'country': self.country,
            'player_id': str(self.player_id),
            'session_id': str(self.session_id),
            'start_ts': str(self.start_ts),
            'end_ts': str(self.end_ts)
        }
