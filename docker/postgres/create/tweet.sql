CREATE TABLE tweets (
  id PRIMARY KEY
  created_at TIMESTAMP NOT NULL,
  full_text TEXT NOT NULL,
  retweeted BOOLEAN,
  in_reply_to_status_id INTEGER,
  in_reply_to_user_id INTEGER,
);
