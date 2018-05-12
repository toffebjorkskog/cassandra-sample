
CREATE TABLE session_start_by_country (
  country text,
  daybucket text,
  start_ts timestamp,
  player_id uuid,
  session_id uuid,
  PRIMARY KEY ((country, daybucket), start_ts)
) WITH CLUSTERING ORDER BY (start_ts DESC);


CREATE TABLE completed_player_sessions_by_player_id (
  player_id uuid,
  start_ts timestamp,
  end_ts timestamp,
  session_id uuid,
  country text,
  PRIMARY KEY (player_id, start_ts)
) WITH CLUSTERING ORDER BY (start_ts DESC);


CREATE TABLE active_sessions_by_session_id (
  session_id uuid,
  player_id uuid,
  start_ts timestamp,
  country text,
  PRIMARY KEY (session_id, start_ts)
) WITH CLUSTERING ORDER BY (start_ts DESC);
