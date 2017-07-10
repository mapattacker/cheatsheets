  
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