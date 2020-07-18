CREATE USER 'travels'@'localhost' IDENTIFIED BY 'tr4v3ls';
DROP DATABASE IF EXISTS Bedutravels;
CREATE DATABASE Bedutravels;
GRANT ALL PRIVILEGES ON Bedutravels.* TO travels@'%' IDENTIFIED BY 'tr4v3ls';
GRANT ALL PRIVILEGES ON Bedutravels.* TO travels@'localhost' IDENTIFIED BY 'tr4v3ls';
FLUSH PRIVILEGES;