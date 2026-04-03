-- Remove user if it exists (prevents failure)
DROP USER IF EXISTS 'user_0d_1'@'localhost';

-- Create user with password
CREATE USER 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost'
WITH GRANT OPTION;

-- Reload privileges
FLUSH PRIVILEGES;
