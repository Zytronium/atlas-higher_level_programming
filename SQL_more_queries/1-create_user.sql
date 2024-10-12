-- creates the MySQL server user user_0d_1 if it doesn't already exist.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVLEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

