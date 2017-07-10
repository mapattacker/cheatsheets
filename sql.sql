  
-- change field name
ALTER TABLE tablename RENAME fieldname1 to fieldname2

--create table
CREATE table public.tablename (
    rule_id int,
    date date,
    consequent varchar,
    support float,
    confidence float,
    lift float,
    support_cnt int);
    
    
--primary keys & indexes
ALTER TABLE tablename ADD PRIMARY KEY (fieldname);
CREATE INDEX indexname ON tablename (fieldname);