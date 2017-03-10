--using Tableau parameters to connect to SQL database with (All) option
with filter_week AS (select 'Weekend' AS weektype, 'Weekend' AS param
									  UNION select 'Weekday' AS weektype, 'Weekday' AS param
									  UNION select 'Weekday' AS weektype, '(All)' AS param
									  UNION select 'Weekend' AS weektype, '(All)' AS param)
SELECT *
FROM DBO.table_nm a
WHERE WEEKTYPE IN (SELECT weektype FROM filter_week WHERE param=:week)
      AND (((is_pub_holiday='N' OR is_pub_holiday='Y') AND :p_holiday='(All)') 
           OR (is_pub_holiday=:p_holiday) OR (is_pub_holiday=:p_holiday))),
