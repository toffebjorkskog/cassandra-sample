import dateutil.parser
import datetime
from player_session_service.core.player_session_manager import (
    get_session_starts_for_country,
    get_latest_player_sessions
)
from player_session_service.models.session_events_by_player_id import (
    SessionEventsByPlayerId,
    StartSessionEvents,
    EndSessionEvents
)
from player_session_service.models.completed_sessions_by_player_id import (
    CompletedSessionsByPlayerId
)
from cassandra.cqlengine.query import DoesNotExist as _DoesNotExist


def get_sample_start_event(
    country='FI',
    player_id='0a2d12a1a7e145de8bae44c0c6e06629',
    session_id='4a0c43c9-c43a-42ff-ba55-67563dfa35d4',
    ts='2016-12-02T12:48:05.520022'
):
    '''
    Function to give you a sample start event.
    You can override default values in the parameters.
    '''
    return {
        'event': 'start',
        'country': country,
        'player_id': player_id,
        'session_id': session_id,
        'ts': ts
    }


def get_sample_end_event(
    country='FI',
    player_id='0a2d12a1a7e145de8bae44c0c6e06629',
    session_id='4a0c43c9-c43a-42ff-ba55-67563dfa35d4',
    ts='2016-12-02T13:33:09'
):
    '''
    Function to give you a sample end event.
    You can override default values in the parameters.
    '''
    return {
        'event': 'end',
        'country': country,
        'player_id': player_id,
        'session_id': session_id,
        'ts': ts
    }


def session_event_exists(player_id, session_id, ty):
    try:
        q = SessionEventsByPlayerId.objects(player_id=player_id,
                                            session_id=session_id)
        events = q.get()
        return len(events) > 0
    except _DoesNotExist:
        return False
    else:
        return False


def session_start_event_exists(player_id, session_id):
    try:
        q = StartSessionEvents.objects(player_id=player_id,
                                       session_id=session_id)
        q.filter(event='start')
        events = q.get()
        return len(events) > 0
    except _DoesNotExist:
        return False
    else:
        return False


def session_end_event_exists(player_id, session_id):
    try:
        q = EndSessionEvents.objects(player_id=player_id,
                                     session_id=session_id)
        q.filter(event='end')
        events = q.get()
        return len(events) > 0
    except _DoesNotExist:
        return False
    else:
        return False


def completed_session_exists(player_id, session_id):
    try:
        q = CompletedSessionsByPlayerId.objects(player_id=player_id,
                                                session_id=session_id)
        events = q.get()
        return len(events) > 0
    except _DoesNotExist:
        return False
    else:
        return False


def count_start_sessions(country_code, hours):
    return len(get_session_starts_for_country(country_code, hours))


def count_player_sessions(player_id):
    return len(get_latest_player_sessions(player_id))


def load_lots_of_events():
    return [{"player_id": "d6313e1fb7d247a6a034e2aadc30ab3f", "country": "PK", "event": "start", "session_id": "674606b1-2270-4285-928f-eef4a6b90a60", "ts": "2016-11-22T20:40:50"}, {"player_id": "20ac16ebb30a477087c3c7501b1fce73", "event": "end", "session_id": "16ca9d01-d240-4527-9f8f-00ef6cddb1d4", "ts": "2016-11-18T06:24:50"}, {"player_id": "318e22b061b54042b880c365c28982d0", "event": "end", "session_id": "5f933591-8cd5-4147-8736-d6237bef5891", "ts": "2016-11-16T18:01:37"}, {"player_id": "29bb390d9b1b4b4b9ec0d6243da34ec4", "event": "end", "session_id": "ef939180-692a-4845-aef7-afb03524c2da", "ts": "2016-11-13T10:38:09"}, {"player_id": "a477ecabc3cc455cb1c6d1dab77d8e5c", "country": "GH", "event": "start", "session_id": "4c55263e-66b2-4814-b431-8ca4c1a9dcc8", "ts": "2016-11-29T19:31:43"}, {"player_id": "1ec36a67785046b3bce1dc432fad9129", "country": "SK", "event": "start", "session_id": "3346a60a-0989-4041-aacc-cf6ff44bd151", "ts": "2016-11-16T05:36:16"}, {"player_id": "9595af0063e94cb8a76cb6628c6b80eb", "country": "DE", "event": "start", "session_id": "06830030-d091-428b-87d6-53914d3d2a18", "ts": "2016-11-07T01:18:09"}, {"player_id": "8d0e3cd4a25d4a0895a6c2e13b5bb26a", "event": "end", "session_id": "a78a4889-4bcf-45a7-a4bd-967cc7adf581", "ts": "2016-11-24T02:12:33"}, {"player_id": "e59f1fa31e144fd8b3634f397492126a", "event": "end", "session_id": "dd223ea6-0e6b-4dd2-bc1d-b2decd43aabf", "ts": "2016-11-13T00:35:30"}, {"player_id": "fd8a1e9fff25471dad3e8ab951c90d60", "event": "end", "session_id": "3015bf71-4b28-4c91-a253-b48607170a1e", "ts": "2016-11-21T01:18:57"}, {"player_id": "5fd71e49d9dc4053b2f3a9adc752982e", "country": "FM", "event": "start", "session_id": "1d9e6d4a-e1c0-4020-b019-a14fb7c665f5", "ts": "2016-11-08T23:39:07"}, {"player_id": "7eaf41e8264946cf9fcb2cbbff001c58", "event": "end", "session_id": "c650360a-3a6c-495c-afcc-ec60f23ad400", "ts": "2016-12-01T10:02:42"}, {"player_id": "4ac6fa82e7a84cad9dbc24360e0c3a64", "country": "SC", "event": "start", "session_id": "b20c6b98-7f18-4bae-8db6-95e36363d244", "ts": "2016-11-24T15:59:10"}, {"player_id": "a34a6188d03746eb867291aefab381de", "country": "KG", "event": "start", "session_id": "c522efe9-847a-47b9-aa5a-85b11fd5f0a7", "ts": "2016-11-13T12:46:31"}, {"player_id": "85b7600411354ff3a1d16b7b828e20ae", "country": "EE", "event": "start", "session_id": "58dd0153-026d-4552-a2c1-dd53373bbf8b", "ts": "2016-11-23T17:49:23"}, {"player_id": "25752b769f5744e98e52f18a93faa09b", "event": "end", "session_id": "94483e5b-bebb-46cd-bfa5-fcc66a0742b0", "ts": "2016-11-16T18:03:50"}, {"player_id": "fc287863d671446dbfdf1bca8debdff5", "event": "end", "session_id": "4f7e416d-fc11-4c39-9b07-62c27e858c19", "ts": "2016-12-01T04:53:15"}, {"player_id": "c408369703f940bb910e10e065f5484a", "event": "end", "session_id": "75cbd945-817a-40aa-aebd-5ebe6d61808e", "ts": "2016-11-10T23:21:49"}, {"player_id": "33e5f534cd074991a01354b95b5b5cf6", "event": "end", "session_id": "9d73326f-800a-466e-a8e4-a000714e9880", "ts": "2016-11-13T04:06:08"}, {"player_id": "03c648a9437d401b8e326cd1f93bd06e", "country": "GS", "event": "start", "session_id": "cd0f2f42-3ab2-4506-bbf7-00f58909b9ef", "ts": "2016-11-29T22:01:36"}, {"player_id": "2e43f27713e14e57a6adb36cd88bc595", "event": "end", "session_id": "4336fdcb-5b40-4654-b87b-f01d960eed5d", "ts": "2016-11-16T15:07:21"}, {"player_id": "d1aeb37eef7c40b491238456faae9eaa", "country": "BN", "event": "start", "session_id": "7d6e9f60-1baf-46e5-893a-367552989e56", "ts": "2016-11-21T09:13:29"}, {"player_id": "3b1bd8dd320647e298b66c7a2558fccc", "country": "NR", "event": "start", "session_id": "18681e89-6c74-4783-a04c-e40e5dd2231b", "ts": "2016-11-14T03:26:29"}, {"player_id": "ca00e428db7541f29fed860c6da7bf5b", "event": "end", "session_id": "4d060036-5cb9-4583-97e7-c2619e5126c6", "ts": "2016-11-19T15:52:52"}, {"player_id": "1b8c9ff2927f4b9598e4893afe589572", "country": "GY", "event": "start", "session_id": "5c4b5d45-7455-4663-84fa-7522fa7b6eb6", "ts": "2016-11-14T07:41:00"}, {"player_id": "afa287764f264351add0d39938bd5989", "country": "SV", "event": "start", "session_id": "eea8018a-5e3f-4df0-a563-515b38d3311c", "ts": "2016-11-15T20:38:07"}, {"player_id": "c6cfdef84b264d7da9215c304737f73e", "event": "end", "session_id": "3e0f6658-f144-42f5-bc84-996a9faa9d06", "ts": "2016-11-17T19:11:25"}, {"player_id": "24a008c2d5084f478639ef2fb9f5b7e2", "event": "end", "session_id": "bb910a41-be71-45f6-9994-dc608622c64c", "ts": "2016-12-01T12:20:17"}, {"player_id": "2c240017adcf4bff9029eac21d179f4c", "event": "end", "session_id": "e086b884-89ac-40a2-90e6-dbfe956b7fdc", "ts": "2016-11-25T01:38:59"}, {"player_id": "3aa403a22f5a40cf8b3a5d4c0e38443c", "event": "end", "session_id": "4694ae13-1af8-47df-bfcf-d124636d8a21", "ts": "2016-11-25T17:26:29"}, {"player_id": "5a57acfbd4f34d45b889f9066e603136", "event": "end", "session_id": "fbfc79c9-c606-41a2-9e35-171e8ec8b61d", "ts": "2016-11-19T01:56:22"}, {"player_id": "584b087454e042688e0ce4f877feb74d", "country": "IS", "event": "start", "session_id": "9983eb04-5dad-4f2e-ad48-37fa0c0ec296", "ts": "2016-11-26T06:11:36"}, {"player_id": "c6c5b57c84274d0c975eaaad6f43708c", "country": "NA", "event": "start", "session_id": "18cf4df6-e2bf-464a-bd06-d601010cf07d", "ts": "2016-11-08T20:33:23"}, {"player_id": "9b4f8903f38b413d8e3541197e445ff5", "country": "UA", "event": "start", "session_id": "62fb7773-0bca-41d5-ab91-9963803adf1a", "ts": "2016-11-28T17:45:34"}, {"player_id": "dc98d84a0fb2447c80281f35af740b11", "country": "GF", "event": "start", "session_id": "f45f8d3c-1833-4a2c-8363-56c4a16066d0", "ts": "2016-11-17T05:05:13"}, {"player_id": "39039247cf6c4178bf678357fa6e07ff", "country": "BE", "event": "start", "session_id": "274d8db0-db7c-4551-8ea8-f06661679604", "ts": "2016-11-04T19:24:50"}, {"player_id": "3c3e48820c294c9d920ecad432928762", "country": "MQ", "event": "start", "session_id": "6634da13-5e47-4efe-81fe-bcb61f98244d", "ts": "2016-11-27T18:48:37"}, {"player_id": "0bd5fdd919134c77b368240f406ec7e9", "event": "end", "session_id": "5bb59154-aead-43eb-b027-264387f324cf", "ts": "2016-11-26T09:45:55"}, {"player_id": "0612127e93ca4ce8bc4478bd86665e87", "event": "end", "session_id": "0d7d27be-2f86-46d0-9e19-dbea5541470d", "ts": "2016-11-29T06:45:53"}, {"player_id": "1206f9573ceb4dd0a814380ae7056539", "event": "end", "session_id": "ce21e390-9a84-473c-b687-af76752a072b", "ts": "2016-12-01T22:05:29"}, {"player_id": "bafd662b59fb40afa18ca5f9b1554577", "country": "PF", "event": "start", "session_id": "a2420886-8fcb-4eda-8a24-44268ce32a05", "ts": "2016-11-14T13:05:43"}, {"player_id": "101d15c43fca4ea0b92df4b460e92218", "event": "end", "session_id": "ea1d53d2-7497-4743-95a1-9f30216fae9f", "ts": "2016-11-26T15:30:25"}, {"player_id": "fef643a1d0dd40cab75b471b72ccaead", "event": "end", "session_id": "453bb88b-1600-49a5-86dc-b4e353fa1695", "ts": "2016-11-24T06:33:35"}, {"player_id": "cef26f7792ac4dc384f0b483bc1bef51", "event": "end", "session_id": "60f7e5ab-76e7-4d68-bbec-1464d771e37e", "ts": "2016-11-18T16:20:39"}, {"player_id": "b23cc01ea54f420fabbb85a133794c76", "country": "VE", "event": "start", "session_id": "69fa20b7-5e59-4170-971f-bda758189df9", "ts": "2016-11-16T03:06:13"}, {"player_id": "06905245f6484e30b5a40c478b7cc72b", "country": "HK", "event": "start", "session_id": "6227e4cb-43a6-4108-952b-d47c9e7002f5", "ts": "2016-11-30T12:27:13"}, {"player_id": "91023ecc2ad747bb8d3b450b9f4a1054", "event": "end", "session_id": "3fb79a44-fec7-4ed1-86aa-21c2b4208865", "ts": "2016-11-14T18:23:37"}, {"player_id": "297011f8e12b4bc89df218017303a10f", "event": "end", "session_id": "5935bb91-7412-4415-86ff-503a5c2c6332", "ts": "2016-11-12T20:47:36"}, {"player_id": "ef26d5b3b7bf40bf9c16da77a5ab7832", "country": "IQ", "event": "start", "session_id": "1c149ac1-02ec-4dc9-9f3c-0a910936b00c", "ts": "2016-11-16T03:43:22"}, {"player_id": "be86a470ac3d4a7c89ea5708b596f9ef", "country": "MV", "event": "start", "session_id": "4dc13d91-d2a9-4e34-a1a3-298d680e11b8", "ts": "2016-11-20T05:47:39"}, {"player_id": "e071d2f3c8b247369963f7136a8d56f8", "country": "ER", "event": "start", "session_id": "0ee0e5b1-36b9-48e6-b0ca-b9a3cd9d9d2f", "ts": "2016-11-20T12:53:42"}, {"player_id": "c20f055fbe494184bafc1dec684ccbda", "country": "AG", "event": "start", "session_id": "bbb731ed-363c-4b5a-ac98-93adb6bac8c1", "ts": "2016-11-30T10:35:35"}, {"player_id": "0d623500ecf84b0884c6ab6fc1d3d3c5", "event": "end", "session_id": "f3635086-4d99-45db-a8b5-edd63339bac4", "ts": "2016-11-30T21:28:28"}, {"player_id": "abff3d2c2bed411b93ccbde96b4d6c60", "country": "JP", "event": "start", "session_id": "5384a303-bf07-4317-b186-54448e12f066", "ts": "2016-11-26T00:52:21"}, {"player_id": "fc8500f670f34127bfc4b76779eaeac0", "event": "end", "session_id": "0aecfa07-c8f4-4fb8-aa87-ce7a8527ca7c", "ts": "2016-11-10T03:10:04"}, {"player_id": "209c6f6509824083a2751c11ddf03e5b", "country": "HU", "event": "start", "session_id": "1dd2f834-9e4c-480f-9d5c-c3d0a3eb98fa", "ts": "2016-11-05T22:43:42"}, {"player_id": "2c8562b7b0db4a4298d06d092d869b45", "country": "TT", "event": "start", "session_id": "aeca87b3-07cf-4804-bb47-b9fc5dcbdb39", "ts": "2016-11-11T13:55:09"}, {"player_id": "71f4bf706e5d48a8b07260d2f2c5f3ad", "country": "SI", "event": "start", "session_id": "681381f1-a7db-4f8f-a02a-6340a4c7790e", "ts": "2016-11-11T05:04:47"}, {"player_id": "b3e4cbbfe627433caa953a215026bd0c", "event": "end", "session_id": "5eebd891-2297-4052-9d41-1080ab35c255", "ts": "2016-11-03T07:21:11"}, {"player_id": "377b39b701ba4f68a821ccad01049ba9", "event": "end", "session_id": "62fe0e39-c179-4dde-967a-5004b813c4cd", "ts": "2016-11-09T07:26:57"}, {"player_id": "0d388e24732b4332b974a9d74fbef7de", "country": "BW", "event": "start", "session_id": "bdb5c5ed-eb0b-4713-876b-bcef724e4be8", "ts": "2016-11-30T01:38:27"}, {"player_id": "25c99e27096c4fb7a99975f0443a3385", "country": "VI", "event": "start", "session_id": "e130fa12-7564-482a-9e07-c3cf8de6d493", "ts": "2016-11-06T11:17:13"}, {"player_id": "4f62af49fd584100949756467ae886bd", "event": "end", "session_id": "9cd48f91-b5a0-4bf6-b444-31ff9d85c589", "ts": "2016-11-28T17:38:07"}, {"player_id": "121ec9451bcc496fa54c736efbbb8dea", "country": "CD", "event": "start", "session_id": "d7ff5bb6-8f12-4bf3-a523-eafdf36d8df9", "ts": "2016-12-01T15:58:38"}, {"player_id": "4b36ed6047eb4aebb008bfe9565eb17d", "event": "end", "session_id": "0b3a95fd-b443-4e75-b263-63445f3ab893", "ts": "2016-11-29T13:22:04"}, {"player_id": "005904c5ff7c45118804f1bd924f73ee", "country": "HR", "event": "start", "session_id": "325e9402-2483-49ca-926d-3d122bd15aea", "ts": "2016-11-04T03:55:52"}, {"player_id": "129049e855724ba986adabfb68a55457", "event": "end", "session_id": "03b24b7f-6e7f-4625-82f6-89c875662591", "ts": "2016-11-26T05:03:14"}, {"player_id": "7fcc307e30214ec298dd6e9f32f34426", "event": "end", "session_id": "388b33bb-3b17-4f3e-a000-8fbf9e86529c", "ts": "2016-11-26T12:01:23"}, {"player_id": "ad6cf62a22184c0c987b1ff1eb3b0958", "event": "end", "session_id": "c3936a62-b744-47c1-80cb-60b609e9d3ea", "ts": "2016-11-20T03:31:20"}, {"player_id": "eac7725364b54a95818fb9aea37ce0d2", "country": "GY", "event": "start", "session_id": "54fb7486-d274-434c-9880-5d0527863d43", "ts": "2016-11-07T09:36:52"}, {"player_id": "6ec11dd945d045c88048719307d42dc1", "event": "end", "session_id": "d3ae15cb-3086-4894-a987-24a2896c604f", "ts": "2016-11-09T13:18:10"}, {"player_id": "9a4fbc2006634e669e2a4fe71466cb8e", "country": "AE", "event": "start", "session_id": "d4544b41-0436-4a88-9c21-af2dd1953f04", "ts": "2016-11-15T07:57:39"}, {"player_id": "8500e7ecc46c414e9886c04a5786cba4", "country": "KR", "event": "start", "session_id": "e1deb355-813d-4b27-b8ed-bd560069ef38", "ts": "2016-11-25T06:07:40"}, {"player_id": "1550490331b245a4820277dd1ddd1d2c", "country": "PT", "event": "start", "session_id": "3aeb41d4-09a9-41bf-8496-d6ecf06c8c73", "ts": "2016-11-11T09:13:54"}, {"player_id": "29ec3002ca3a4bcf997d8e70676fbe86", "country": "GS", "event": "start", "session_id": "5cb8eb4b-836b-477a-a7a8-d5e2a28b82f5", "ts": "2016-11-09T21:22:55"}, {"player_id": "d5219229faf04f18b5945a4037bf4a29", "event": "end", "session_id": "3ac94c2d-f9df-4b0a-b176-87866b36b743", "ts": "2016-11-25T02:11:21"}, {"player_id": "0b7206f9a8b74abf835aba4e8b8df587", "event": "end", "session_id": "933a4f77-8b85-429d-8882-8c8775d0beb9", "ts": "2016-11-24T06:38:44"}, {"player_id": "5232926533354dffb2ed242ba19d7bb2", "country": "MP", "event": "start", "session_id": "261bcf52-a213-46f1-9333-a73d7dbf4d78", "ts": "2016-11-28T05:55:05"}, {"player_id": "f07fd4291be941bcbf56abae37fb43cb", "country": "BV", "event": "start", "session_id": "5dbe7f58-76ce-4e4a-af64-01a5fd0392c6", "ts": "2016-11-11T23:54:03"}, {"player_id": "022f2b5bc6ef4a12846a6f9ec4ba763b", "country": "WF", "event": "start", "session_id": "ed4be4af-45c3-476e-873f-0ab4383b8370", "ts": "2016-11-13T11:23:49"}, {"player_id": "e2eddd6b0bf94ae585ed7ce106ecbac1", "event": "end", "session_id": "dc74237c-5768-436c-92b9-861f7806f0fc", "ts": "2016-11-17T15:21:53"}, {"player_id": "5f98cb4667be443fa6e88e4de4d84c2d", "country": "SX", "event": "start", "session_id": "4aea6c37-3996-45e5-9700-9536a0426cd5", "ts": "2016-11-09T02:28:47"}, {"player_id": "1aecc8b4f1934d54afc0c3f86a8e9a32", "event": "end", "session_id": "53a03bf2-1f27-474d-bea1-fda0ba2c3730", "ts": "2016-11-22T15:44:24"}, {"player_id": "0229a943d4a74bff824c33612432087d", "country": "WF", "event": "start", "session_id": "774ccc05-377e-4272-827c-651b397c5c05", "ts": "2016-11-08T06:19:39"}, {"player_id": "99526b2fd61b4d5081bc8b0bebb5af8b", "country": "GH", "event": "start", "session_id": "d8184405-7c68-483c-9016-d7f494a5a9b3", "ts": "2016-11-26T05:47:53"}, {"player_id": "515300c4e9a54a059b137ac7dfec517a", "country": "ID", "event": "start", "session_id": "8b0dc786-76f5-424f-a7de-d87e7251268a", "ts": "2016-11-04T20:59:53"}, {"player_id": "575d718fccf9491590fbe6c4b05266c1", "country": "VA", "event": "start", "session_id": "fcc4fefa-f489-4fec-929c-669497576200", "ts": "2016-11-11T23:05:24"}, {"player_id": "23f53c791eab40da90dfed4b7da35551", "event": "end", "session_id": "0d544151-4b07-484e-a0b2-1346a78dd825", "ts": "2016-11-19T04:23:58"}, {"player_id": "26444086d2904ed9a24fbcafd9d089c6", "country": "DE", "event": "start", "session_id": "648753ea-c074-490e-bf1c-996a45b72e8a", "ts": "2016-11-26T23:47:55"}, {"player_id": "21cc36aeeb4f49a78c0d0b0e4460efc5", "event": "end", "session_id": "1877a057-e291-4f90-9323-85103feed0f3", "ts": "2016-11-02T23:41:00"}, {"player_id": "2ef538c1b8714ba2b3546eab2b1ba3ec", "country": "NR", "event": "start", "session_id": "bafbb6d3-2ba6-4e69-88c2-de151cd790d9", "ts": "2016-11-27T11:51:16"}, {"player_id": "e0879c63c43448c28b0f5745a1a69f98", "event": "end", "session_id": "e52c6c38-8d1a-4630-b3e4-fdeff6609923", "ts": "2016-11-03T15:15:45"}, {"player_id": "bef7ccb5ec9c48abb034c4bf4516b88f", "country": "GD", "event": "start", "session_id": "dc0b0c29-fca5-4e5b-aaa6-2b7351d90ce2", "ts": "2016-11-20T04:34:15"}, {"player_id": "e0712dcdabd349a68903f3913df51e3f", "event": "end", "session_id": "7c381e1a-f9ca-4960-9894-464f08d08bbc", "ts": "2016-11-23T10:10:12"}, {"player_id": "866a47cd580443aead8f5763f5fc082e", "country": "KR", "event": "start", "session_id": "679d33fd-4ad2-4cef-91b1-2f549402dc9a", "ts": "2016-11-23T11:54:37"}, {"player_id": "58f792abec714e47908deebeebcd4d44", "country": "GB", "event": "start", "session_id": "16794879-0d8b-47ef-b80b-3ad0dcd1d8e2", "ts": "2016-11-21T09:56:14"}, {"player_id": "0bb416bfd6634c6e8e2930966ec6ceb5", "event": "end", "session_id": "21b71e1e-7949-4e93-805d-3504160604ce", "ts": "2016-11-27T03:49:03"}, {"player_id": "5310621db6074aa39cbe68c1c1dae19c", "country": "GI", "event": "start", "session_id": "b495b363-47eb-4974-935c-e11494aa4dba", "ts": "2016-11-29T12:25:17"}, {"player_id": "c1373ba60630421baffad6bb506836ac", "country": "BA", "event": "start", "session_id": "78d0ce61-6081-4e79-ad60-db43a82e098f", "ts": "2016-11-18T11:56:09"}, {"player_id": "a711108edf4444ca8e1179e4d5f2923c", "country": "DE", "event": "start", "session_id": "82ce524c-3a00-4ccd-871e-cadec8012661", "ts": "2016-11-09T15:14:32"}]
