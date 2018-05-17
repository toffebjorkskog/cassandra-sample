# module conftest.py
# This fixture config is baed upon the github issue for pytest-flask:
# https://github.com/pytest-dev/pytest-flask/issues/70#issuecomment-361005780
# by @kenshiro-o

import pytest

from player_session_service import create_app
from player_session_service.models import db as _db
from cassandra.cqlengine.management import (
    drop_keyspace, create_keyspace_simple
)


@pytest.fixture(scope="session")
def app(request):
    """
    Returns session-wide testing application.
    """
    return create_app("testing")  # important parameter


@pytest.fixture(scope="session")
def db(app, request):
    """
    Returns session-wide initialised database.
    """
    with app.app_context():
        _reset_db(app, _db)
        return _db


def _reset_db(app, db):
    """
    Returns session-wide reset db
    """
    drop_keyspace(app.config['CASSANDRA_KEYSPACE'])
    create_keyspace_simple(app.config['CASSANDRA_KEYSPACE'],
                           replication_factor=1)

    # create the tables from out models.
    db.sync_db()


@pytest.fixture(scope="function", autouse=True)
def session(app, db, request):
    """
    resets session
    """
    with app.app_context():
        _reset_db(app, db)

