# SQLProjects

CREATE TABLE friends(
  id INTEGER,
  name TEXT,
  birthday DATE
);

INSERT INTO friends (id, name, birthday) VALUES (1, 'Ororo Munroe', '1940-05-30');

INSERT INTO friends (id, name, birthday) VALUES (2, 'David Johnson', '1981-09-01');

INSERT INTO friends (id, name, birthday) VALUES (3, 'Zack Johnson', '1994-04-23');

UPDATE friends
SET name = 'Storm'
WHERE id = 1;

ALTER TABLE friends 
ADD COLUMN email TEXT; 

UPDATE friends
SET email = 'storm@codecademy.com'
WHERE id = 1;

UPDATE friends
SET email = 'david@codecademy.com.'
WHERE id = 2;

UPDATE friends
SET email = 'zack@codecademy.com.'
WHERE id = 3;

DELETE FROM friends where id = 1;

SELECT * FROM friends; 
