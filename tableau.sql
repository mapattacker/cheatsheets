--------------------------------------SQL---------------------------------------
--using Tableau parameters to connect to SQL database
-- with (All) option
	--either define a table with possible and (All) attributes, and define in WHERE clause
with filter_week AS (select 'Weekend' AS weektype, 'Weekend' AS param
			  UNION select 'Weekday' AS weektype, 'Weekday' AS param
			  UNION select 'Weekday' AS weektype, '(All)' AS param
			  UNION select 'Weekend' AS weektype, '(All)' AS param)
SELECT * FROM DBO.table_nm a
WHERE WEEKTYPE IN (SELECT weektype FROM filter_week WHERE param=:week);

	--or just entirely in the WHERE clause as below
WHERE (((time_belt='Morning' OR time_belt='Day' OR time_belt= 'Evening') AND :timebelt='(All)') OR (time_belt=:timebelt))

---------------------------------------
--Define Date range
WHERE trunc(DATE_TIME) BETWEEN :strt_1_tme and :end_1_tme;
--Define Time range
WHERE (to_char(DATE_TIME,'hh24:mi') between :stme1 and :etme1))

---------------------------------------
--Set date as constant so that Tableau can group by time only
SELECT to_char(DATE_TIME, '1900-01-01 HH24:MI')::timestamp
FROM table_nm


---------------------------------------
--graph networks; set a unidirectional & bidirectional graph according to time in a day
	--paired movement to next location by time series
with origin as (select user_id, timestamp, location, day_type, time_belt,
					--pair the next (end) ap by time sequence partition by day
					lead(ap_name) over(partition by user_id, date order by timestamp) as loc_end, 
					--row_number() over(partition by user_mac, start_date order by start_timestamp) as seq_id
				from main_table
				where location is not null 
				order by user_id, timestamp),
	 --define if this is a unidirectional or bidirectional count using least & greatest (postgresql)
	 direction AS (SELECT * FROM (SELECT user_id, start_timestamp, least(location,loc_end), day_type, time_belt, greatest(location, loc_end) FROM origin)
	 				WHERE :direction = 'Unidirectional'
	 				UNION SELECT * FROM origin WHERE :direction = 'Bidirectional'),
	 --get total count of movement for each ap-ap permutation
	 movement as (select location as loc_start, 1 as path_order, day_type, time_belt, loc_end, 2 as path_order2,
	 					 --create unique path id when start & end ap is the same
	 					 --row_number()over() as path_id, count(*),
	 					 dense_rank()over(order by location, loc_end) as path_id, count(*),
	 					 (case when location = loc_end then 1 else 0 end) as test
			  from direction group by location, loc_end, day_type, time_belt),
	 --remove those which start & end aps are the same, and those start and end ap that are null
	 remove as (select * from movement where test = 0 and loc_end is not null),
	 --stack ap end below ap start to conform to tableau mapping format
	 stack as (select * from (select day_type, time_belt, loc_start as location, loc_start, loc_end, path_order, path_id, count from remove)a
	 			  union 
	 		   	  select * from (select day_type, time_belt, loc_start as location, loc_start, loc_end, path_order2 as path_order, path_id, count from remove)b)
select *, b.latitude, b.longitude 
from stack a
join table_coordinates b on a.fieldnm = b.fieldnm


	--find most common path
with newtable as (select * from (select *, 
                   --for testing & removing adjacent duplicated connections in same location
                    (CASE when lead(path) over(partition by user1 order by timestamp) = path then 1
                      else 0 end) as test
                  from table1 order by 1,3)a
                  where test = 0),
      --group concat of each corresponding path
      group_concat as (select user1, string_agg(path, '>' order by timestamp) 
                       from newtable
                      group by user1)
select string_agg, count(*) from group_concat
group by string_agg

--------------------------------------TABLEAU---------------------------------------
--Tableau Field Calculations

--adjustable time bin aggregation
  --(1) Set date as constant so that Tableau can group by time only
DATEADD('second', DATEDIFF('second', DATETRUNC('day',[Date Time]), [Date Time]), #1900-01-01#)
  --(2) field calculation (Time Bins)
DATEADD('minute', 
	INT(DATEDIFF('minute', DATETRUNC('day', [YF : Time]), [YF : Time]) / [Minute Bin Size] 
     	    ) * [Minute Bin Size], 
DATETRUNC('day', [YF : Time]))
  --(3) set an integer parameter with range for changing bin size
