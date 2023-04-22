create database PYcapstone;
use PYcapstone;
create table pokedata
(id int NOT NULL primary key,
name char(30),
Description char(255),
type1 char(30),
type2 char(30)
);

// Import the Pokemon CSV or JSON File.

select * from pokedata;
