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
    # FLASK_APP_CONFIG_FILE points to
    if 'FLASK_APP_CONFIG_FILE' in os.environ:
        app.config.from_envvar('FLASK_APP_CONFIG_FILE')

    # Override CASSANDRA_HOSTS from environment variable.
    if 'CASSANDRA_HOSTS' in os.environ:
        app.config['CASSANDRA_HOSTS'] = os.getenv('CASSANDRA_HOSTS', '127.0.0.1').split(',')


    # Finally, allow keyspace to be overridden via app factory paramter
    if KEYSPACE_OVERRIDE is not None:
        app.config['CASSANDRA_KEYSPACE'] = KEYSPACE_OVERRIDE

    models.init_app(app)
    apis.init_app(app)

    return app
