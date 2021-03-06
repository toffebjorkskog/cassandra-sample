from flask_restplus import Api
from .player_events import api as player_events
from .country_sessions import api as country_sessions
from .player_sessions import api as player_sessions


def init_app(app):
    api = Api(
        title='Player Session Service',
        version='1.0',
        description='This service which consumes events and provides metrics '
                    'about players sessions. Each user will generate two '
                    'events, one start event when the session starts and one '
                    'end event when session is finished. When both events '
                    'have been received the session is considered complete. '
                    'This Service is expected to handle massive amount of '
                    'sessions.',
    )
    api.add_namespace(player_events, path='/player-session-service')
    api.add_namespace(country_sessions, path='/player-session-service')
    api.add_namespace(player_sessions, path='/player-session-service')
    # Add similar row for more endpoints...

    api.init_app(app)
