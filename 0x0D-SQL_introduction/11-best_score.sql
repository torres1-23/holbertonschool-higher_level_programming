-- List all records from a table with a threshold score.
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
