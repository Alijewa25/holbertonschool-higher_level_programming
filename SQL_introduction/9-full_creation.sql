-- script that performs a specific task
-- script that performs a specific task
-- Create a TABLE called `second_TABLE` and INSERT a row into it.
CREATE TABLE IF NOT EXISTS second_TABLE (
  id INT,
  name VARCHAR(256),
  score INT
);

INSERT INTO second_TABLE (id, name, score) VALUES
  (1, 'John', 10),
  (2, 'Alex', 3),
  (3, 'Bob', 14),
  (4, 'George', 8);
