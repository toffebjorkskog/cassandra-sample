import pytest
from player_session_service.core.validation import validate_start_event


def test_validate_start_event__missing_parameters__event():
    event = {
            'player_id': '02a0511372394597aa76c89f106aa547',
            'country': 'AE',
            'session_id': 'e0d836e6-2128-436b-a689-38c47a477118',
            'ts': '2016-11-06T03:11:56'
    }
    with pytest.raises(TypeError) as e_info:
        validate_start_event(event)


def test_validate_start_event__missing_parameters__player_id():
    event = {
            'country': 'AE',
            'event': 'start',
            'session_id': 'e0d836e6-2128-436b-a689-38c47a477118',
            'ts': '2016-11-06T03:11:56'
    }
    with pytest.raises(TypeError) as e_info:
        validate_start_event(event)


def test_validate_start_event__missing_parameters__country():
    event = {
            'player_id': '02a0511372394597aa76c89f106aa547',
            'event': 'start',
            'session_id': 'e0d836e6-2128-436b-a689-38c47a477118',
            'ts': '2016-11-06T03:11:56'
    }
    with pytest.raises(TypeError) as e_info:
        validate_start_event(event)


def test_validate_start_event__missing_parameters__session_id():
    event = {
            'player_id': '02a0511372394597aa76c89f106aa547',
            'country': 'AE',
            'event': 'start',
            'ts': '2016-11-06T03:11:56'
    }
    with pytest.raises(TypeError) as e_info:
        validate_start_event(event)


def test_validate_start_event__missing_parameters__ts():
    event = {
            'player_id': '02a0511372394597aa76c89f106aa547',
            'country': 'AE',
            'event': 'start',
            'session_id': 'e0d836e6-2128-436b-a689-38c47a477118',
    }
    with pytest.raises(TypeError) as e_info:
        validate_start_event(event)


def test_validate_start_event__wrong_parameters__ts():
    event = {
            'player_id': '02a0511372394597aa76c89f106aa547',
            'country': 'AE',
            'event': 'start',
            'session_id': 'e0d836e6-2128-436b-a689-38c47a477118',
            'ts': '2016-00-06T03:11:56'

    }
    with pytest.raises(ValueError) as e_info:
        validate_start_event(event)


def test_validate_start_event__wrong_parameters__non_uuid_player_id():
    event = {
            'player_id': '02a05GÖÖÖÖ1372394597aa76c89f106aa547',
            'country': 'AE',
            'event': 'start',
            'session_id': 'e0d836e6-2128-436b-a689-38c47a477118',
            'ts': '2016-11-06T03:11:56'

    }
    with pytest.raises(ValueError) as e_info:
        validate_start_event(event)


def test_validate_start_event__wrong_parameters__non_uuid_session_id():
    event = {
            'player_id': '02a0511372394597aa76c89f106aa547',
            'country': 'AE',
            'event': 'start',
            'session_id': 'e0d83Öe6-2128-436b-a689-38c47a477118',
            'ts': '2016-11-06T03:11:56'

    }
    with pytest.raises(ValueError) as e_info:
        validate_start_event(event)


def test_validate_start_event__wrong_parameters__invalid_countrycode():
    event = {
            'player_id': '02a0511372394597aa76c89f106aa547',
            'country': 'AEE',
            'event': 'start',
            'session_id': 'e0d836e6-2128-436b-a689-38c47a477118',
            'ts': '2016-11-06T03:11:56'

    }
    with pytest.raises(ValueError) as e_info:
        validate_start_event(event)
