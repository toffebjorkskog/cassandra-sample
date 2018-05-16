from flask_cassandra import CassandraCluster
from cassandra.cqlengine.connection import setup as setup_cassandra
from . import session_start_by_country


def init_app(app):
    cluster = CassandraCluster(app)
    session = cluster.connect('player_sessions')
    return (cluster, session)


def setup_schema():
    from cassandra.cqlengine.management import sync_table
    sync_table(SessionStartByCountry)
