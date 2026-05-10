-- Select the id and name of cities that belong to California
-- The database name will be passed as an argument
SELECT id, name FROM cities
WHERE state_id = (
    SELECT id FROM states
    WHERE name = 'California'
)
ORDER BY id ASC;