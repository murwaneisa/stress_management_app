-- Create Database -- 
DROP DATABASE IF EXISTS `stresstracker`;

CREATE DATABASE `stresstracker`;
USE `stresstracker`;

-- Create Users table --
DROP TABLE IF EXISTS `user`;


CREATE TABLE `user` (
user_id int(11) NOT NULL AUTO_INCREMENT,
user_username varchar(70),
user_firstname varchar(70),
user_lastname varchar(70),
user_gender char(1),
user_email varchar(70),
user_program varchar(130),
user_degree varchar(130),
user_password varchar(100),
user_dob date,
user_studystart int(4),
PRIMARY KEY (user_id))ENGINE=INNODB;

INSERT INTO `user` (user_id,user_username,user_firstname,user_lastname,user_gender,user_email, user_program,user_degree,user_password,user_dob,user_studystart)
VALUES (1,'test','Test','User','X','test@hotmail.com','Computer Science','Bachelor','$2b$12$Cq/7WpaizowelsSrmMBidOIAKdzhrLiPSxsBLTcGncXWkaBoNYiE.','1900-1-1',2021),
(2,'meisa','Murwan','Eisa','M','meisa@hotmail.com','Computer Science','Bachelor','$2b$12$JVwVF/ESZdfwPM5jQBm6e.1Kdpjaxi7Fp4ek1loIAgW1rNpxXSgWO','1990-1-1',2021),
(3,'ctoth','Cameron','Toth','F','toth123@hotmail.com','Computer Science','Bachelor','$2b$12$stBRqc3Bw4Oaao/T2yONte/bPWgJ5UuodnWFJsAJj6EVRe8lHKVyu','1995-1-1',2021);


-- Create Stats table --
DROP TABLE IF EXISTS `stats`;


CREATE TABLE `stats` (
stats_id int(11) NOT NULL AUTO_INCREMENT,
stats_userid int(11),
stats_year int(4),
stats_weeknr int(2),
stats_sleep int(4),
stats_study int(4),
stats_work int(4),
stats_social int(4),
stats_sport int(4),
stats_hobby int(4),
stats_stress int(4),
stats_migraine int(4),
stats_digest int(4),
stats_insomnia int(4),
stats_energy int(4),
stats_relation int(4),
stats_financial int(4),
stats_comments varchar(200),
PRIMARY KEY (stats_id),
FOREIGN KEY (stats_userid) REFERENCES user(user_id))ENGINE=INNODB;

INSERT INTO `stats` (stats_id,stats_userid,stats_year,stats_weeknr,stats_sleep,stats_study,stats_work,stats_social,stats_sport,stats_hobby,stats_stress,stats_migraine,stats_digest,stats_insomnia,stats_energy,stats_relation,stats_financial,stats_comments)
VALUES (1,2,2022,15,8,30,8,4,2,4,4,0,0,0,0,0,0,""),
(2,2,2022,16,10,40,8,2,2,4,3,0,0,0,0,0,0,""),
(3,2,2022,17,8,25,8,5,3,4,4,0,0,1,0,0,0,""),
(4,3,2022,18,9,35,8,2,1,3,5,0,0,1,0,0,0,""),
(5,3,2022,15,6,45,0,8,3,3,2,0,0,0,0,0,0,""),
(6,3,2022,16,6,30,0,8,3,4,2,2,0,0,0,0,0,""),
(7,3,2022,17,4,20,0,6,3,6,3,1,0,0,0,0,0,""),
(8,3,2022,18,8,25,0,10,3,8,5,0,0,3,0,0,0,"");

CREATE TABLE `admin` (
admin_id int(11) NOT NULL AUTO_INCREMENT,
admin_username varchar(70),
admin_firstname varchar(70),
admin_lastname varchar(70),
admin_email varchar(70),
admin_password varchar(100),
PRIMARY KEY (admin_id))ENGINE=INNODB;

INSERT INTO `admin` (admin_id,admin_username,admin_firstname,admin_lastname,admin_email,admin_password)
VALUES (1,'kallej','Kalle','Johan','kallej@hotmail.com','$2b$12$RGPABi7kzqkRSbjdaRYAw.hCfjOcMkEHOJzA.N3FnsTwC4GPa5xhC');


CREATE TABLE `avg_stats` (
stats_id int(11) NOT NULL AUTO_INCREMENT,
stats_userid int(11),
stats_bound int(1),
stats_program varchar(130),
stats_degree varchar(130),
stats_sleep int(4),
stats_study int(4),
stats_work int(4),
stats_social int(4),
stats_sport int(4),
stats_hobby int(4),
PRIMARY KEY (stats_id),
FOREIGN KEY (stats_userid) REFERENCES admin(admin_id))ENGINE=INNODB;

INSERT INTO `avg_stats` (stats_id,stats_userid,stats_bound,stats_program,stats_degree,stats_sleep,stats_study,stats_work,stats_social,stats_sport,stats_hobby)
VALUES (1,1,0,'Computer Science','Bachelor',8,30,0,5,2,5),
(2,1,1,'Computer Science','Bachelor',12,45,16,10,10,10),
(3,1,0,'Default','Default',8,30,0,5,2,5),
(4,1,1,'Default','Default',12,45,16,10,10,10);
