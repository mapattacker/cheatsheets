--SYSTEM----------------------
--check list of tables in database
SELECT * FROM information_schema.tables 
--check version of database
select version() 
--check index tables
SELECT * FROM pg_indexes 
WHERE schemaname = 'public' and tablename = 'mytable';


--EXECUTION PLAN----------------------
--prints the time started for query to execute
explain analyze 
select query

--use this awesome visualizer to view the plan
--http://tatiyants.com


--VACUUM----------------------
--clean up junk in table that can affect performance
vacuum analzye table_name


--NEW TABLE----------------------
--time series
SELECT date_trunc('day', dd)::date
FROM generate_series
        ('2007-02-01'::timestamp, 
         '2008-04-01'::timestamp,
         '1 day'::interval) dd

--numbers
select generate_series(1,4)


--CROSS JOIN----------------------
select date, count from
--table 1
(SELECT date_trunc('day', dd)::date as date
 FROM generate_series ('2017-01-01'::timestamp, 
	               '2017-02-28'::timestamp, 
                       '1 day'::interval) dd) a
cross join
--table 2
(select generate_series(1,4) count) b


--HISTOGRAM BINNING----------------------
--width_bucket(column_name, start_range, end_range, no_of_bins)
--note, any values that fall out of start or end range will be classified into another bin
select width_bucket(columName, 0, 0.25, 10) as output_bin_no, 
	count(*), 
	min(columName),
	max(columName),
from tablename
group by 1
order by 1


--DATES-----------------------------
--get year
extract(year from to_timestamp(starttime))
date_part('year', to_timestamp(starttime))
--get month
extract(month from to_timestamp(starttime))
date_part('month', to_timestamp(starttime))
--get week no. of month
select ((date_part('day', now()::date)::integer-1)/7)+1
to_char(to_timestamp(starttime), 'W')
