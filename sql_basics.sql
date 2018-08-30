--SCHEMATICS
--------------------------------------
--Create Database
CREATE DATABASE tablename
  DEFAULT CHARACTER SET utf8;

--User Access
  --can specific CRUD specific access rights too
GRANT ALL ON misc.* TO 'fred'@'localhost' IDENTIFIED BY 'zap';
  

--Create Schema
CREATE SCHEMA schema_name;
CREATE SCHEMA AUTHORIZATION user_name;

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

UPDATE species_info --update replace multiple rows
SET column_name = REPLACE(column_name, 'Image', 'image') 

--update from another table selection
INSERT INTO table2 (column1, column2, column3, ...)
SELECT column1, column2, column3, ...
FROM table1
WHERE condition;


--delete rows
DELETE FROM ts_biz_100m_ap; --delete entire table
DELETE FROM Customers 
  WHERE CustomerName='Alfreds Futterkiste';

UPDATE table_name
  SET your_column_name = NULL; --not really delete but to purge data in a column

--query column names from a table
SELECT column_name,* 
FROM information_schema.columns
WHERE table_name = 'wsg_radius_log'


--create views
CREATE VIEW view_name AS
select * from tablename
where column 1 


--QUERIES
--------------------------------------
--select consecutive before & after rows
select *,
      lead(column_nm) over(partition by column_nm2 order by column_nm3), --selects the row below the current
      lead(column_nm) over(partition by column_nm2 order by column_nm3), --selects the row above the current
from table_name 

--if else
select (case when column1 - column2 >= 14 then 1 else 0 END) as difference
from table_name


-- JOIN
--------------------------------------
-- join using where clause
select a.name, b.grade, a.marks
from students a, grades b
where a.marks between b.min_Mark and b.Max_Mark --joined using a between


--CONVERT DATA TYPE
--------------------------------------
  --simple conversion (POSTGRES, VERTICA)
select column1::date, column2::int
  --using CAST (IMPALA)
select CAST('2016-02-03 06:37:51' as timestamp)


--AGGREGATE FUNCTIONS
--------------------------------------
--number of rows is reduced
--must group by column names that are not aggregated in selected columns
select sum(sales), salesperson
from tableName
group by salesperson
order by 1


--ANALYTIC FUNCTIONS
--------------------------------------
--no change in total rows
select sum(sales) over (partition by salesperson order by column_nm)
from tableName



--DATETIME
--------------------------------------
--CONVERT TO DATETIME
  --from EPOCH to TIMESTAMP (IMPALA)
select to_timestamp(1456314748) 
  --from TIMESTAMP to DATE (IMPALA)
select to_date(now())
  --from string to TIMESTAMP
select CAST('2016-02-03 06:37:51' as timestamp)
  --fixed constant parts for datetime
select to_char(starttime, '1900-01-01 HH24:00:00')::timestamp --(POSTGRES)
select cast(concat('1991-01-01', ' ', from_unixtime(1392394861, 'HH'), ':00:00') as timestamp) --(IMPALA)


--DATETIME DELTA (ADD/DIFF)
select now() - interval '15 minutes' -- (POSTGRES)
select now() - interval 15 minutes -- (IMPALA)
select datediff(day, startdate, enddate)


--TRUNCATE
select trunc(starttime, 'dd')


--EXTRACT (POSTGRES, IMPALA)
select extract(now(), 'year');
  --2017
  
  
-- SUBQUERY
--------------------------------------
-- WITH CLAUSE
  --easily readable and recommended for initial scripting. however performance issues, so need to change to real subquery after coding
with table1 as (select *
                from tablenm
                where column1 = 'stop')
select * 
from table1



with table1 as (select * from tablenm where col1 > 10),
     table2 as (select * from tablenm where col2 = 'sex')
select * from table1 a
join table2 b on a.col1 = b.col1


-- SUBQUERY
  --very difficult to interpret when query is long. But performance is optimised.
select * 
from (select *
      from tablenm
      where column1 = 'stop') a


-- WHERE
--------------------------------------
  -- using IN clause for multiple values
SELECT column_name(s)
FROM table_name
WHERE column_name IN (value1, value2, ...)


-- NEW COLUMNS
--------------------------------------
  -- row number
select row_number() over(order by name), name from occupations 

  -- lead & lag
select hacker_id, name, cnt, 
        lag(cnt) over(order by cnt desc, hacker_id asc) as lag,
        lead(cnt) over(order by cnt desc, hacker_id asc) as lead
from table1

--USEFUL QUERIES
--------------------------------------
-- MODULUS
select distinct city
from station
where id %2=0 --only even numbers


-- show # duplicate rows
select column1, column2, count(*)-1 as duplicate_cnt
from wsg_radius_log
group by column1, column2
having count(*) > 0

-- delete duplicated rows
DELETE users 
WHERE rowid NOT IN (
  -- set a row_number
  with rownm as (select row_number() over() as rowid, * 
                  from tablename)
    -- only keep a unique, non-duplicate row defined by min. rowid 
  select min(rowid)
  from rownm
  GROUP BY date, file_name -- add all columns necessary to define duplicates
  order by 2, 3) a