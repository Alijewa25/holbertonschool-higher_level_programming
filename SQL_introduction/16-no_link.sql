-- script that performs a specific task
-- List row with score by descending and name from the second_TABLE only if name is valid
SELECT score, name FROM second_TABLE WHERE name IS NOT NULL ORDER BY score DESC;
