--SCHEMATICS
--------------------------------------
--Create Database
CREATE DATABASE tablename
  DEFAULT CHARACTER SET utf8;

--Alter Existing Table
ALTER TABLE tablename RENAME fieldname1 to fieldname2
ALTER TABLE table_name ADD fieldname float;

--Create Table
CREATE table tablename (
    id int not null auto_increment,
    rule_id int unsigned, --unsigned = +ve
    date date,
    consequent varchar,
    support float,
    confidence float,
    lift float,
    support_cnt int,
    primary key (id),
    index(rule_id)
    );

CREATE table newtable (
    artist_id int not null auto_increment
    artist varchar(128), 
    album_id int,
    
    primary key(artist_id)
    constraint foreign key(album_id) references album(album_id)
      on delete cascade on update cascade,
    );

--Add Primary keys & Indexes
ALTER TABLE tablename ADD PRIMARY KEY (fieldname);
CREATE INDEX indexname ON tablename (fieldname);

--insert
insert into operator_lookup(user_nm_domain, operator) values ('y5zwew.sg','testdata');

--update
UPDATE Customers
SET ContactName = 'Alfred Schmidt', City= 'Frankfurt'
WHERE CustomerID = 1;

--delete all data from table
delete from ts_biz_100m_ap;

--query column names from a table
SELECT column_name,* 
FROM information_schema.columns
WHERE table_name = 'wsg_radius_log'


--QUERIES
--------------------------------------
--select consecutive before & after rows
select *,
      lead(column_nm) over(partition by column_nm2 order by column_nm3), --selects the row below the current
      lead(column_nm) over(partition by column_nm2 order by column_nm3), --selects the row above the current
from table_name 

--if else
select (case when column1 - column2 >= 14 then 1 else 0) as difference
from table_name

--Union
