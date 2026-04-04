-- script that performs a specific task
-- script that performs a specific task
-- List the number of times each score appears in the second_TABLE
SELECT score, COUNT(*) AS number
FROM second_TABLE
GROUP BY score
ORDER BY number DESC;
