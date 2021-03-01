-- Lists all records of a table of a database.
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC
