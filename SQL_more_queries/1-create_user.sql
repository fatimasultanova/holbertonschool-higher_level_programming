-- Create the user if they do not exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges without the 'WITH GRANT OPTION'
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Ensure changes are applied
FLUSH PRIVILEGES;