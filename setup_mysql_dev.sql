-- Creates a new database for the project.
-- Creates a new user in localhost and sets password.
-- Set privileges on the database.
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON DATABASE 'hbnb_dev_db' TO 'hbnb_dev';
GRANT SELECT ON 'performance_schema' TO 'hbnb_dev';