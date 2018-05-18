import dateutil.parser
from uuid import UUID


def validate_start_event(event):
    '''
    Raises TypeError for missing attributes and ValueError for incorrect values
    '''
    for key in ['event', 'player_id', 'country', 'session_id', 'ts']:
        if key not in event.keys():
            raise TypeError('Missing attribute: {}'.format(key))

    if event['event'] != 'start':
        raise ValueError('Invalid event attribute, allowed values are "start" and "end"')

    dateutil.parser.parse(event['ts'])  # naturally raises exception..

    UUID(event['player_id'])
    UUID(event['session_id'])

    if len(event['country']) != 2:
        raise ValueError('Invalid country code: {}'.format(event['country']))


def validate_end_event(event):
    '''
    Raises TypeError for missing attributes and ValueError for incorrect values
    '''
    for key in ['event', 'player_id', 'session_id', 'ts']:
        if key not in event.keys():
            raise TypeError('Missing attribute: {}'.format(key))

    if event['event'] != 'end':
        raise ValueError('Invalid event attribute, allowed values are "start" and "end"')

    dateutil.parser.parse(event['ts'])  # naturally raises exception..

    UUID(event['player_id'])
    UUID(event['session_id'])

