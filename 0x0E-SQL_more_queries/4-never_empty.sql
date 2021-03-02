-- Creates a table on a MYSQL server.
-- Table id_not_null with columns id default value 1 and name.
CREATE TABLE
    IF NOT EXISTS id_not_null(
        id INT DEFAULT 1,
        name VARCHAR(256) 
    );
