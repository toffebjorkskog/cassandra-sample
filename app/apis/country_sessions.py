from flask import request

from flask_restplus import Namespace, Resource, fields
from ..core.player_session_manager import (insert_player_events,
                                           get_session_starts_for_country)

api = Namespace('Sessions per Country', description='For retrieving sessions '
                'for the last X hours per country')

# Api response type.
start_sessions = api.model('Start Sessions', {
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
})


# Api endpoints
@api.route('/started-sessions/<country_code>/<hours>')
class StartedSessionsPerCountry(Resource):
    @api.doc('per_country')
    # @api.marshal_list_with(start_sessions)
    def get(self, country_code, hours):
        '''
        Retrieve start events for the last X hours and given country.
        '''
        try:
            sessions = get_session_starts_for_country(country_code, hours)
            return {'session_starts': sessions}, 200
        except Exception as e:
            return {'status': 'Bad Request', 'message': str(e)}, 400
