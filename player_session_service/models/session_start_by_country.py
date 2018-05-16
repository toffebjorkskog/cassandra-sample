from ..models import db


class SessionStartByCountry(db.Model):
    __table_name_case_sensitive__ = 'session_start_by_country'
    __default_ttl__ = 31536000
    country = db.columns.Text(partition_key=True, primary_key=True)
    daybucket = db.columns.Text(partition_key=True, primary_key=True)
    start_ts = db.columns.DateTime(primary_key=True)
    player_id = db.columns.UUID(required=True)
    session_id = db.columns.Text(required=True)
