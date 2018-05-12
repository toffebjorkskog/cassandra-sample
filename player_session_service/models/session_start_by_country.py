from cassandra.cqlengine.models import Model
from cassandra.cqlengine import columns


class SessionStartByCountry(Model):
    __table_name_case_sensitive__ = 'session_start_by_country'
    __keyspace__ = 'player_sessions'
    country = columns.Text(partition_key=True, primary_key=True)
    daybucket = columns.Text(partition_key=True, primary_key=True)
    start_ts = columns.DateTime(primary_key=True)
    player_id = columns.UUID()
    session_id = columns.UUID()
