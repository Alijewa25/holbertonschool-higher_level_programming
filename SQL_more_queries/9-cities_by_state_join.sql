-- Select city id, city name, and state name
SELECT cities.id, cities.name, states.name
FROM cities

-- Join cities with states using the foreign key relationship
JOIN states ON cities.state_id = states.id

-- Sort results by city id in ascending order
ORDER BY cities.id ASC;
