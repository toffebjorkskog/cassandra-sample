import pytest
from player_session_service.core.player_session_manager import (
    insert_start_event, insert_end_event, insert_player_events
)
from player_session_service.models.session_events_by_player_id import (
    SessionEventsByPlayerId
)
from helpfunctions import (
    get_sample_start_event, get_sample_end_event, session_event_exists,
    session_start_event_exists, session_end_event_exists,
    completed_session_exists, load_lots_of_events, count_start_sessions,
    count_player_sessions
)
from faker import Faker
from datetime import datetime, timedelta


def test_create_start_event__event_is_added_to_cassandra():
    event = get_sample_start_event(
        player_id='00000000000000000000000000000001',
        session_id='00000000-0123-4567-8910-000000000001'
    )

    state_before = session_start_event_exists(player_id=event["player_id"],
                                              session_id=event["session_id"])
    insert_start_event(event)
    state_after = session_start_event_exists(player_id=event["player_id"],
                                             session_id=event["session_id"])

    assert state_before is False and state_after is True


def test_create_end_event__event_is_added_to_cassandra():
    event = get_sample_end_event(
        player_id='00000000000000000000000000000009',
        session_id='00000000-0123-4567-8910-000000000009'
    )

    state_before = session_end_event_exists(player_id=event["player_id"],
                                            session_id=event["session_id"])
    insert_end_event(event)
    state_after = session_end_event_exists(player_id=event["player_id"],
                                           session_id=event["session_id"])

    assert state_before is False and state_after is True


def test_create_start_event__uuid_is_prettified():
    event = get_sample_start_event(
        player_id='02a0511372394597aa76c89f106aa547',
        session_id='00000000-0123-4567-8910-000000000002'
    )

    returndata = insert_start_event(event)

    uuid_with_dashes = '02a05113-7239-4597-aa76-c89f106aa547'
    assert str(returndata['player_session']['player_id']) == uuid_with_dashes


def test_create_start_and_end_event__completed_session_is_added_to_cassandra():
    player_id = '00000000000000000000000000000003'
    session_id = '00000000-0123-4567-8910-000000000003'
    start_event = get_sample_start_event(player_id=player_id,
                                         session_id=session_id)
    end_event = get_sample_end_event(player_id=player_id,
                                     session_id=session_id)

    completed_state_before = completed_session_exists(player_id, session_id)
    insert_start_event(start_event)
    insert_end_event(end_event)

    completed_state_after = completed_session_exists(player_id, session_id)
    assert completed_state_before is False and completed_state_after is True


def test_create_end_first_then_start_event__completed_session_added_to_db():
    player_id = '00000000000000000000000000000004'
    session_id = '00000000-0123-4567-8910-000000000004'
    start_event = get_sample_start_event(player_id=player_id,
                                         session_id=session_id)
    end_event = get_sample_end_event(player_id=player_id,
                                     session_id=session_id)

    completed_state_before = completed_session_exists(player_id, session_id)
    # the other way around.
    insert_end_event(end_event)
    insert_start_event(start_event)

    completed_state_after = completed_session_exists(player_id, session_id)
    assert completed_state_before is False and completed_state_after is True


def test_create_start_event_only__no_completed_session_added_to_db():
    player_id = '00000000000000000000000000000005'
    session_id = '00000000-0123-4567-8910-000000000005'
    start_event = get_sample_start_event(player_id=player_id,
                                         session_id=session_id)

    completed_state_before = completed_session_exists(player_id, session_id)
    # I dont insert end event.
    insert_start_event(start_event)

    completed_state_after = completed_session_exists(player_id, session_id)
    assert completed_state_before is False and completed_state_after is False


def test_insert_player_events__pass_more_than_10_events__throws_exception():
    events = load_lots_of_events()  # A HUNDRED! :P
    with pytest.raises(ValueError):
        insert_player_events(events)


def test_insert_player_events__pass_zero_events__throws_exception():
    events = []
    with pytest.raises(ValueError):
        insert_player_events(events)


def test_insert_player_events__pass_1_to_10_events__does_not_throw_exception():
    events = load_lots_of_events()
    for i in range(0, 9):
        insert_player_events(events[i*10:i*10+i+1])
    assert True


def test_get_session_starts_for_country__prepolulates_with_10__gets_10():
    amount_before = count_start_sessions(country_code='FI', hours=48)

    player_id = '000000000000000000000000000000{}'  # lacks 2 digits
    session_id = '00000000-0123-4567-8910-0000000000{}'  # lacks 2 digits
    event = {
        'event': 'start',
        'country': 'FI',
    }
    fake = Faker()

    for i in range(10, 20):
        event['player_id'] = player_id.format(i)
        event['session_id'] = session_id.format(i)
        event['ts'] = str(fake.date_time_between(start_date='-2d',
                                                 end_date='now'))
        start_event = insert_start_event(event)

    amount_after = count_start_sessions(country_code='FI', hours=48)

    if amount_before == 0 and amount_after == 10:
        assert True
    else:
        pytest.fail("before: {}, after:{}".format(amount_before, amount_after))


def test_get_player_sessions__prepolulates_with_10__gets_10():
    player_id = '00000000000000000000000000000030'
    amount_before = count_player_sessions(player_id=player_id)

    session_id = '00000000-0123-4567-8910-0000000000{}'  # lacks 2 digits
    event = {
        'event': 'start',
        'country': 'FI',
        'player_id': player_id
    }
    fake = Faker()
    for i in range(20, 30):
        ts = fake.date_time_between(start_date='-2d', end_date='-1h')
        event['session_id'] = session_id.format(i)
        event['ts'] = str(ts)
        start_event = insert_start_event(event)
        event2 = event.copy()
        event2['ts'] = str(ts + timedelta(hours=1))
        event2['event'] = 'end'
        end_event = insert_end_event(event2)

    amount_after = count_player_sessions(player_id=player_id)

    if amount_before == 0 and amount_after == 10:
        assert True
    else:
        pytest.fail("before: {}, after:{}".format(amount_before, amount_after))
