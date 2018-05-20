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
pipenv install --dev
```

And then launch the API
```
pipenv run server
```

## <a name="configuration"></a>Configuration
The default configuration settings are located in `player_session_service/config/default_settings.cfg`.
The settings can be overriden by pointing the environment variable `PLAYER_SESSION_SERVICE_SETTINGS` to a similar config file.


## Testing
Get sample data to the project root folder:
```
wget https://cdn.example.com/sample_data.jsonl.bz2 -O - | bunzip2 > sample-data.jsonl
```

For Unit testing, run:
```
pipenv run test
```
The tests come in two parts: unit testing with pytest, and api testing using `tavern-ci`
which tests the REST-endpoints. Both are run by pytest using the previous command.
Unit testing uses its own "testing" keyspace, but the api testing uses the one that the flask app
is currently using.
Note: The unit test assumes that the provided sample data `sample_data.jsonl` file is in the root folder of the project.
