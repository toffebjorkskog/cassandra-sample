from flask import Flask
import os
from .config import TestingConfig, DevelopmentConfig, ProductionConfig

config_options = {
    "development": DevelopmentConfig,
    "testing": "config.TestingConfig",
    "production": "config.ProductionConfig",
}


def create_app(KEYSPACE_OVERRIDE=None):
    from . import apis, core, models
    app = Flask(__name__)

    # Load default settings
    config_name = os.getenv('FLASK_ENV', 'development')
    app.config.from_object(config_options[config_name])

    # Override defaults settings from file that env variable
    # PLAYER_SESSION_SERVICE_SETTINGS points to
    if 'PLAYER_SESSION_SERVICE_SETTINGS' in os.environ:
        app.config.from_envvar('PLAYER_SESSION_SERVICE_SETTINGS')

    # Finally, allow keyspace to be overridden via app factory paramter
    if KEYSPACE_OVERRIDE is not None:
        app.config['CASSANDRA_KEYSPACE'] = KEYSPACE_OVERRIDE

    models.init_app(app)
    apis.init_app(app)

    return app
