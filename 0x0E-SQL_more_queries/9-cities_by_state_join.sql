-- Lists all cities contained in database passed as argument.
-- Display record way: citites.id cities.name states.name.
-- Sorted by cities.id in ASC.
SELECT cities.id, cities.name, states.name
    FROM cities
    INNER JOIN states
    ON cities.state_id = states.id
ORDER BY id ASC;
