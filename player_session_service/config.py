class BaseConfig(object):
    DEBUG = True
    TESTING = False
    CASSANDRA_HOSTS = ['127.0.0.1']
    CASSANDRA_KEYSPACE = 'player_sessions'
    #CASSANDRA_CONSISTENCY = 'QUORUM'
    #CASSANDRA_SETUP_KWARGS = {'protocol_version': 3}
    #CASSANDRA_LAZY_CONNECT = True   # True - should not connect until firstuse
    #CASSANDRA_RETRY_CONNEC = False  # True means reconnect even when failure
    SECRET_KEY = 'qpwkedfvdöojfödskg'  # override this in production
    CASSANDRA_REPLICATION_FACTOR = 1

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    CASSANDRA_KEYSPACE = 'player_sessions_development'


class TestingConfig(BaseConfig):
    DEBUG = False
    TESTING = True
    CASSANDRA_KEYSPACE = 'player_sessions_testing'


class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False
    CASSANDRA_KEYSPACE = 'player_sessions_production'
    CASSANDRA_REPLICATION_FACTOR = 3
