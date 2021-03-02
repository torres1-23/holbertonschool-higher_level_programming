-- Creates a table unique_id in a MYSQL server.
-- Column id with default value 1 and unique and name.
CREATE TABLE
    IF NOT EXISTS unique_id(
        id INT UNIQUE DEFAULT 1,
        name VARCHAR(256) 
    );
