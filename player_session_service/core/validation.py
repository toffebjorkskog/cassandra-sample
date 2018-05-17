def validate_start_event(event):
    if 'event' in event.keys():
        if event['event'] not in ['start', 'end']:
            raise ValueError('Invalid event value, it should be "start" or "end"')
    else:
        raise TypeError('Missing attribute: event')

