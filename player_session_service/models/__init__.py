from flask_cqlalchemy import CQLAlchemy
from cassandra.cqlengine.management import (
    create_keyspace_simple
)
db = CQLAlchemy()


def init_app(app):
    db.init_app(app)
    create_keyspace_simple(
        app.config['CASSANDRA_KEYSPACE'],
        replication_factor=app.config['CASSANDRA_REPLICATION_FACTOR']
    )
    db.sync_db()
