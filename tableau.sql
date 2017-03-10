--using Tableau parameters to connect to SQL database with (All) option
	--either define a table with possible and (All) attributes, and define in WHERE clause
with filter_week AS (select 'Weekend' AS weektype, 'Weekend' AS param
			  UNION select 'Weekday' AS weektype, 'Weekday' AS param
			  UNION select 'Weekday' AS weektype, '(All)' AS param
			  UNION select 'Weekend' AS weektype, '(All)' AS param)
SELECT * FROM DBO.table_nm a
WHERE WEEKTYPE IN (SELECT weektype FROM filter_week WHERE param=:week);

	--or just entirely in the WHERE clause as below
SELECT * FROM DBO.table_nm a
WHERE (((holiday='N' OR holiday='Y') AND :holiday='(All)') OR (holiday=:holiday));

---------------------------------------
--Define Date range
WHERE trunc(a.DATE_TIME) BETWEEN :strt_1_tme and :end_1_tme;
--Define Time range
WHERE (to_char(a.DATE_TIME,'hh24:mi') between :stme1 and :etme1))
