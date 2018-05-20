from flask import Flask
import os


def create_app(KEYSPACE_OVERRIDE=None):
    from . import apis, core, models
    app = Flask(__name__)

    # Load default settins
    app.config.from_pyfile('default_settings.cfg')

    # Override defaults settings from file that env variable
    # PLAYER_SESSION_SERVICE_SETTINGS points to
    if 'PLAYER_SESSION_SERVICE_SETTINGS' in os.environ:
        app.config.from_envvar('PLAYER_SESSION_SERVICE_SETTINGS')

    # Finally, allow keyspace to be overridden via app factory paramter
    # This is used by pytest fo runittesting
    if KEYSPACE_OVERRIDE is not None:
        app.config['CASSANDRA_KEYSPACE'] = KEYSPACE_OVERRIDE

    models.init_app(app)
    apis.init_app(app)

    return app
