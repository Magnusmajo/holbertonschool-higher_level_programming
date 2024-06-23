-- in database
-- Create database and table

CREATE DATABASE hbtn_0d_usa;

CREATE TABLE hbtn_0d_usa.cities(
    'id' INT NOT NULL AUTO_INCREMENT UNIQUE,
    'state_id' INT NOT NULL,
    'name' VARCHAR(256) NOT NULL,
    PRIMARY KEY('id')
    FOREIN KEY ('state_id') REFERENCES states ('id')
);