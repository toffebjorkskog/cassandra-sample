# Sample Cassandra REST-API

## Installation

```
virtualenv -p `which python3` venv
source .env
pip install -r requirements.txt
```

```
$ source .env
$ python run.py
```



## Testing
For Unit testing, run:
```
pytest player_session_service/tests/core
```
For Continuous Integration Testing of the REST-API, run the following:
```
tavern-ci --stdout player_session_service/tests/apis/*.yaml
```
To run both in one command, run:
```
./test.sh
```
