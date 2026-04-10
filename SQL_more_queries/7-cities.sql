-- Create the database if it does not already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Select the database to use
USE hbtn_0d_usa;

-- Create the table cities if it does not already exist
CREATE TABLE IF NOT EXISTS cities (
    -- id: unique identifier, auto-incremented, primary key, not null
    id INT AUTO_INCREMENT PRIMARY KEY,

    -- state_id: references states.id, cannot be null
    state_id INT NOT NULL,

    -- name: city name, cannot be null
    name VARCHAR(256) NOT NULL,

    -- Foreign key constraint linking to states table
    FOREIGN KEY (state_id) REFERENCES states(id)
);
