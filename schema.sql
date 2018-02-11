DROP TABLE IF EXISTS albums;
CREATE TABLE albums (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  artist STRING NOT NULL,
  name STRING NOT NULL
  release_date DATE NOT NULL
);