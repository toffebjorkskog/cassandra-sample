from flask import request

from flask_restplus import Namespace, Resource, fields
from ..core.player_session_manager import (insert_player_events,
                                           get_session_starts_for_country)

api = Namespace('Player Events and Sessions', description='Player Events related operations')

event = api.model('Player Event', {
    'event': fields.String(
        required=True,
        description='start|end'
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
        description='Player id, example: 4a0c43c9-c43a-42ff-ba55-67563dfa35d4'
    ),
    'ts': fields.DateTime(
        required=True,
        description='Start or end Timestamp'
    ),
})

player_events_schema = api.schema_model('PlayerEvents', {
    'type': 'array',
    'items': {
        'type': 'object',
        'properties': {
            'event': {
                'type': 'string',
                'enum': ['start', 'end']
            },
            'country': {
                'type': 'string',
                'minLength': 2,
                'maxLength': 2,
            },
            'player_id': {
                'type': 'string'
            },
            'session_id': {
                'type': 'string'
            },
            'ts': {
                'type': 'string',
                'format': 'date-time',
            },
        },
        'minItems': 1,
        'maxItems': 10,
        'required': ['event', 'player_id', 'session_id', 'ts']
    }
})


@api.route('/player-events/')
class PlayerSessionEvents(Resource):
    @api.doc('Player Event')
    @api.expect(player_events_schema, validate=True)
    #@api.marshal_list_with(event)
    def post(self):
        '''Submit event batches (1-10 events / batch)'''
        try:
            insert_player_events(request.get_json())
            return {'status': 'Created'}, 201
        except Exception as e:
            return {'status': 'Bad Request', 'message': str(e)}, 400
