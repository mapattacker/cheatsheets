--make new table, time series
SELECT date_trunc('day', dd)::date
FROM generate_series
        ('2007-02-01'::timestamp, 
         '2008-04-01'::timestamp,
         '1 day'::interval) dd
