-- Creates a database hbtn_0d_usa.
-- Table states
-- Columns id INT, unique, auto, not null and is a primary key.
-- name 256 bytes long not null.
CREATE DATABASE
    IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE
    IF NOT EXISTS hbtn_0d_usa.states(
        id INT UNIQUE NOT NULL AUTO_INCREMENT,
        name VARCHAR(256) NOT NULL,
        PRIMARY KEY (id)
    );
