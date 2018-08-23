CREATE TABLE nowonsale  (
  saleid SERIAL PRIMARY KEY,
  starttime TIMESTAMP,
  endtime TIMESTAMP,
  title TEXT NOT NULL,
  URL TEXT
)
