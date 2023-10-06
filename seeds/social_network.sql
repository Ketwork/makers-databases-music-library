-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT,
    email TEXT
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO users (username, email) VALUES ('ket', 'ket@ket.net');
INSERT INTO users (username, email) VALUES ('User 2', 'user2@ket.net');


-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title TEXT,
    content TEXT,
    views INT,
    user_id INT
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO posts (title, content, views, user_id) VALUES ('my title 1', 'My Content', 0, 1);
INSERT INTO posts (title, content, views, user_id) VALUES ('my title 2', 'My Content', 0, 2);
