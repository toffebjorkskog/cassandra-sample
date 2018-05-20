from app.models import db


class SessionStartsByCountry(db.Model):
    __table_name_case_sensitive__ = 'session_starts_by_country'
    __default_ttl__ = 31536000
    country = db.columns.Text(partition_key=True, primary_key=True)
    daybucket = db.columns.Text(partition_key=True, primary_key=True)
    start_ts = db.columns.DateTime(primary_key=True, clustering_order='DESC')
    player_id = db.columns.UUID(required=True)
    session_id = db.columns.UUID(required=True)

    def get_data(self):
        return {
            'type': 'start',
            'country': self.country,
            'player_id': str(self.player_id),
            'session_id': str(self.session_id),
            'ts': str(self.start_ts)
        }
