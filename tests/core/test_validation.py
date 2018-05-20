import pytest
from app.core.validation import (
    validate_start_event, validate_end_event
)
from helpfunctions import get_sample_start_event, get_sample_end_event


'''
Testing validation of start events:
'''


def test_validate_start_event__valid_event_should_not_raise_error():
    event = get_sample_start_event()
    try:
        validate_start_event(event)
        assert True
    except:
        pytest.fail("Valid start event raised exception")


def test_validate_start_event__missing_event():
    event = get_sample_start_event()
    del event['event']
    with pytest.raises(TypeError) as e_info:
        validate_start_event(event)


def test_validate_start_event__missing_player_id():
    event = get_sample_start_event()
    del event['player_id']
    with pytest.raises(TypeError) as e_info:
        validate_start_event(event)


def test_validate_start_event__missing_country():
    event = get_sample_start_event()
    del event['country']
    with pytest.raises(TypeError) as e_info:
        validate_start_event(event)


def test_validate_start_event__missing_session_id():
    event = get_sample_start_event()
    del event['session_id']
    with pytest.raises(TypeError) as e_info:
        validate_start_event(event)


def test_validate_start_event__missing_ts():
    event = get_sample_start_event()
    del event['ts']
    with pytest.raises(TypeError) as e_info:
        validate_start_event(event)


def test_validate_start_event__invalid_ts():
    event = get_sample_start_event()
    event['ts'] = '2016-00-06T03:11:56'
    with pytest.raises(ValueError) as e_info:
        validate_start_event(event)


def test_validate_start_event__invalid_player_id():
    event = get_sample_start_event()
    event['player_id'] = '02a05GÖÖÖÖ1372394597aa76c89f106aa547'
    with pytest.raises(ValueError) as e_info:
        validate_start_event(event)


def test_validate_start_event__invalid_session_id():
    event = get_sample_start_event()
    event['session_id'] = 'e0d83Öe6-2128-436b-a689-38c47a477118'
    with pytest.raises(ValueError) as e_info:
        validate_start_event(event)


def test_validate_start_event__invalid_country_format():
    event = get_sample_start_event()
    event['country'] = 'AAE'
    with pytest.raises(ValueError) as e_info:
        validate_start_event(event)


'''
Testing validation of end events
'''


def test_validate_end_event__valid_event_should_not_raise_error():
    event = get_sample_end_event()
    try:
        validate_end_event(event)
        assert True
    except:
        pytest.fail("Valid end event raised exception")


def test_validate_end_event__missing_event():
    event = get_sample_end_event()
    del event['event']
    with pytest.raises(TypeError) as e_info:
        validate_start_event(event)


def test_validate_end_event__missing_player_id():
    event = get_sample_end_event()
    del event['player_id']
    with pytest.raises(TypeError) as e_info:
        validate_start_event(event)


def test_validate_end_event__missing_session_id():
    event = get_sample_end_event()
    del event['session_id']
    with pytest.raises(TypeError) as e_info:
        validate_start_event(event)


def test_validate_end_event__missing_ts():
    event = get_sample_end_event()
    del event['ts']
    with pytest.raises(TypeError) as e_info:
        validate_start_event(event)
