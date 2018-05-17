# Sample Cassandra REST-API

## Installation

### For local development without Docker
Install and start Cassandra.
By default a local single node on localhost is assumed. You can also connect to a cluster.
If you want to connect to an external node or cluster, see _configuraton_ section
```
cassandra -f
```
And then launch the API
```
source .env
pip install -r requirements.txt
flask run
```

## Configuration
The default configuration settings are located in `player_session_service/config/default_settings.cfg`.
The settings can be overriden by pointing the environment variable `PLAYER_SESSION_SERVICE_SETTINGS` to a similar config file.


## Testing
For Unit testing, run:
```
pytest
```
For Continuous Integration Testing of the REST-API, run the following:
```
tavern-ci --stdout tests/apis/*.tavern.yaml
```
