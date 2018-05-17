'''
  module conftest.py

  See
  http://flask.pocoo.org/docs/1.0/testing/
  https://docs.pytest.org/en/latest/fixture.html
  and
  https://github.com/pytest-dev/pytest-flask/issues/70#issuecomment-361005780
'''

import pytest

from player_session_service import create_app
from player_session_service.models import db as _db
from cassandra.cqlengine.management import (
    drop_keyspace, create_keyspace_simple
)


@pytest.fixture
def client():
    assert False == True
    '''db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
    flaskr.app.config['TESTING'] = True
    client = flaskr.app.test_client()

    with flaskr.app.app_context():
        flaskr.init_db()

    yield client

    os.close(db_fd)
    os.unlink(flaskr.app.config['DATABASE'])'''


@pytest.fixture(scope="session")
def app(request):
    """
    Returns session-wide testing application.
    """
    app = create_app("testing")  # important parameter
    return app

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
