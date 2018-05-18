# Sample Cassandra REST-API

## Installation

### For local development without Docker
Install and start Cassandra.
By default a local single node on localhost is assumed. You can also connect to a cluster.
If you want to connect to an external node or cluster, see _configuraton_ section
```
cassandra -f
```
set up vitual environment and install required packages.
```
source .env
pip install -r requirements.txt
```

set up database if you are using local standalone cassandra node:
```
python setup.py
```

And then launch the API
```
flask run
```

## Configuration
The default configuration settings are located in `player_session_service/config/default_settings.cfg`.
The settings can be overriden by pointing the environment variable `PLAYER_SESSION_SERVICE_SETTINGS` to a similar config file.


## Testing
For Unit testing, run:
```
python -m pytest
```
For Continuous Integration Testing of the REST-API, run the following:
```
tavern-ci --stdout tests/apis/*.tavern.yaml
```
