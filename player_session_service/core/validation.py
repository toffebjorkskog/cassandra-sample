import dateutil.parser


def validate_start_event(event):
    for key in ['event', 'player_id', 'country', 'session_id', 'ts']:
        if key not in event.keys():
            raise TypeError('Missing attribute: {}'.format(key))

    if event['event'] not in ['start', 'end']:
        raise ValueError('Invalid event attribute, allowed values are "start" and "end"')

    dateutil.parser.parse(event['ts'])  # naturally raises exception..
