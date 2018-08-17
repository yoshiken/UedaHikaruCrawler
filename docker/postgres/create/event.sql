CREATE TABLE event (
  eventid SERIAL PRIMARY KEY,
  day DATE,
  title TEXT NOT NULL,
  doortime TIME,
  showtime TIME,
  closetime TIME,
  location TEXT,
  imgname TEXT,
  love INTEGER
);
