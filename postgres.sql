
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
