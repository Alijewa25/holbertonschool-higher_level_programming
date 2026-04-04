-- script that performs a specific task
-- List score by descending order from the second_TABLE only if the score is greater or equal to 10
SELECT `score`, `name` FROM `second_TABLE` WHERE `score` >= 10 ORDER BY `score` DESC;
