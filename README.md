# Sample Cassandra REST-API

## Installation

### For local development without Docker
Install and start Cassandra.
By default a local single node on localhost is assumed. You can also connect to a cluster.
If you want to connect to an external node or cluster, see [_configuraton_](#configuration) section
```
cassandra -f
```
Install depemndencies with [pipenv](https://docs.pipenv.org/)
```
pipenv install
```

And then launch the API
```
pipenv run server
```

## <a name="configuration"></a>Configuration
The default configuration settings are located in `player_session_service/config/default_settings.cfg`.
The settings can be overriden by pointing the environment variable `PLAYER_SESSION_SERVICE_SETTINGS` to a similar config file.


## Testing
For Unit testing, run:
```
pipenv run test
```
