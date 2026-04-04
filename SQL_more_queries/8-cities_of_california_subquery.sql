-- Select city id and name from cities table
SELECT id, name
FROM cities

-- Filter cities where state_id matches California's id
WHERE state_id = (
    -- Subquery to get the id of the state named California
    SELECT id
    FROM states
    WHERE name = 'California'
)

-- Sort results by city id in ascending order
ORDER BY id ASC;
