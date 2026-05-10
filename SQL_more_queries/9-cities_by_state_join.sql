-- Select city ID, city name, and state name using a JOIN
-- Results are sorted by cities.id in ascending order
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;