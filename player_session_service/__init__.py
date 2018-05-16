from flask import Flask
import os


def create_app():
    from . import apis, core, models
    app = Flask(__name__)

    app.config.from_pyfile('default_settings.cfg')
    if 'PLAYER_SESSION_SERVICE_SETTINGS' in os.environ:
        app.config.from_envvar('PLAYER_SESSION_SERVICE_SETTINGS')

    apis.init_app(app)
    models.init_app(app)

    return app
