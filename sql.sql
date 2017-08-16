  
--Alter Existing Table
ALTER TABLE tablename RENAME fieldname1 to fieldname2
ALTER TABLE table_name ADD fieldname float;

--Create Table
CREATE table public.tablename (
    rule_id int,
    date date,
    consequent varchar,
    support float,
    confidence float,
    lift float,
    support_cnt int);

--Primary keys & Indexes
ALTER TABLE tablename ADD PRIMARY KEY (fieldname);
CREATE INDEX indexname ON tablename (fieldname);

--QUERIES
--------------------------------------

--select consecutive before & after rows
select *,
      lead(column_nm) over(partition by column_nm2 order by column_nm3), --selects the row below the current
      lead(column_nm) over(partition by column_nm2 order by column_nm3), --selects the row above the current
from table_name 

--conditional selection

(CASE when lag(ap_name) over(partition by user_mac, start_date order by start_timestamp) = ap_name then 1 else 0 end)

