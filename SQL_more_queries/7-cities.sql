-- in database
-- Create database and table

CREATE DATABASE hbtn_0d_usa;
USE hbtn_0d_usa;

CREATE TABLE cities(
    'id' INT NOT NULL PRIMARY KEY AUTO_INCREMENT UNIQUE,
    'state_id' INT NOT NULL,
    FOREIN KEY ('state_id') REFERENCES states ('id'),
    'name' VARCHAR(256) NOT NULL
);