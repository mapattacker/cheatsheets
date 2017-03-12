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
--graph networks
create table table1 (
  id integer,
  node1 varchar,
  node2 varchar,
  count numeric);

insert into table1 (id,node1,node2,count) values (1,'0135weqwe','0146w468',10);
insert into table1 (id,node1,node2,count) values (2,'0146w468','0135weqwe',20);
insert into table1 (id,node1,node2,count) values (3,'qwe46587','0146w468',30);
insert into table1 (id,node1,node2,count) values (4,'qwe46587','0135weqwe',30);
insert into table1 (id,node1,node2,count) values (5,'0135weqwe','qwe46587',20);
insert into table1 (id,node1,node2,count) values (6,'0146w468','qwe46587',10);
	--changing bidirectional to unidirectional; use least and greatest.
with table2 as (select id, least(node1, node2) as node1, greatest(node1, node2) as node2, count
             	from table1)
select node1, node2, sum(count)
from table2
group by node1, node2
order by 3


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
