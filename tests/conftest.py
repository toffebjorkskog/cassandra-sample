'''
  module conftest.py

  See
  http://flask.pocoo.org/docs/1.0/testing/
  https://docs.pytest.org/en/latest/fixture.html
  and
  https://github.com/pytest-dev/pytest-flask/issues/70#issuecomment-361005780
'''
import pytest
from app import create_app
from app.models import db as _db
from cassandra.cqlengine.management import (
    drop_keyspace, create_keyspace_simple
)


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
    '''
    Get a clean and empty database.
    When testing, the app is initiated with keyspace 'testing'
    '''
    drop_keyspace(app.config['CASSANDRA_KEYSPACE'])
    create_keyspace_simple(app.config['CASSANDRA_KEYSPACE'],
                           replication_factor=1)

    # create the tables from our models.
    db.sync_db()


@pytest.fixture(scope="function", autouse=True)
def session(app, db, request):
    """
    Resets session. We want a clean empty db for each (py)test.
    """
    with app.app_context():
        _reset_db(app, db)
