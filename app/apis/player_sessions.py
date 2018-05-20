from flask import request

from flask_restplus import Namespace, Resource, fields
from ..core.player_session_manager import (insert_player_events,
                                           get_latest_player_sessions)

api = Namespace('Player Sessions', description='For retrieving the last 20 '
                'completed sessions for a user')

# Api response type.
player_sessions = api.model('Player Sessions', {
    'event': fields.String(
        required=False,
        description='completed'
    ),
    'country': fields.String(
        required=False,
        description='Country code, example: FI'
    ),
    'player_id': fields.String(
        required=True,
        description='Player id, example: 0a2d12a1a7e145de8bae44c0c6e06629'
    ),
    'session_id': fields.String(
        required=True,
        description='Session id, example: 4a0c43c9-c43a-42ff-ba55-67563dfa35d4'
    ),
    'start_ts': fields.DateTime(
        required=True,
        description='Start or end Timestamp'
    ),
    'end_ts': fields.DateTime(
        required=True,
        description='Start or end Timestamp'
    ),
})


# Api endpoints
@api.route('/player-sessions/<player_id>')
class PlayerSessions(Resource):
    @api.doc('player_sessions')
    # @api.marshal_list_with(start_sessions)
    def get(self, player_id):
        '''
        Retrieve the last 20 completed sessions for a player
        '''
        try:
            sessions = get_latest_player_sessions(player_id)
            return {'player_sessions': sessions}, 200
        except Exception as e:
            return {'status': 'Bad Request', 'message': str(e)}, 400
