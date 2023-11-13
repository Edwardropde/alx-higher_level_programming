-- Create db 'hbtn_0d_usa'
-- If db already exists, script should not fail
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;


-- Create table 'states' in db 'hbtn_0d_usa'
-- id INT unique auto-generated not null and primary key
-- name VARCHAR(256) not null
-- If table already exists, script should not fail
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`states` (
	PRIMARY KEY(`id`),
	`id`   INT          NOT NULL AUTO_INCREMENT,
	`name` VARCHAR(256) NOT NULL
);
