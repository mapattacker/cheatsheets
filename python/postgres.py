import psycopg2
conn = psycopg2.connect("dbname=dq user=sq password=eRqg123EEkl") #OR
conn = psycopg2.connect(dbname="dq", user="sq", password="eRqg123EEkl")
cur = conn.cursor()


# USERS ----------------
# new user
cur.execute("CREATE USER data_viewer WITH PASSWORD 'somepassword' NOSUPERUSER")
# revoke privileges
cur.execute('REVOKE DROP ON accounts FROM new_user')
# grant privileges
cur.execute('GRANT DROP ON accounts FROM new_user')


# user groups
cur.execute("CREATE GROUP readonly NOLOGIN")
cur.execute("REVOKE ALL ON user_accounts FROM readonly")
cur.execute("GRANT SELECT ON user_accounts TO readonly")
cur.execute("GRANT readonly TO data_viewer")




# SCHEMA ----------------
# 3 schema types -----
# pg_catalog: system catalog tables
# information_schema: information schema tables
# public: default schema for user created tables

# using namespace
cur.execute('SELECT * FROM ihw.hurricanes') 
cur.execute('SELECT * FROM hud.developments')

# get all table names
cur.execute('''
select table_name from information_schema.tables order by table_name
''')

# get only user created tables
cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public'")

table_names = cur.fetchall()
for i in table_names:
    print(i)


# for inserting strings into a table name
from psycopg2.extensions import AsIs #need this function so wont change to string during insertion
cur.execute('select * from %s limit 0', [AsIs(table)]) # must be list or tuple in 2nd argument

# get description of table
cur.execute('select * from ign_reviews limit 0')
print(cur.description)



# EXPLAIN & ANALYZE----------------
# http://tatiyants.com/pev/#/plans, use this visualizer
# explain is only an estimate
import pprint as pp
cur.execute("explain (format json) select count(*) from homeless_by_coc where year > '2012-1-1'")
pp.pprint(cur.fetchall())


# explain analyze is an actual benchmark
cur.execute("explain analyze select count(*) from homeless_by_coc where year>'2012-01-01'") #OR
cur.execute("explain (analyze, format json) select count(*) from homeless_by_coc where year>'2012-01-01'")

# query plan
# Each cost is an estimated value that is measured as an arbitary unit of time but not an actual value, like ms.
[
   {
     "Plan": {
       "Node Type": "Aggregate",
       "Strategy": "Plain",
       "Startup Cost": 2490.33, #time it takes before a rows can be returned (something like sorting, or collecting the rows and aggregating them)
       "Total Cost": 2490.34, #includes startup cost. total time it takes to run the node plan until completion
       "Plan Rows": 1,
       "Plan Width": 0,
       "Actual Startup Time": 305.209,
       "Actual Total Time": 305.211,
       "Actual Rows": 1,
       "Actual Loops": 1,
       "Plans": [
         {
           "Node Type": "Seq Scan",
           "Parent Relationship": "Outer",
           "Relation Name": "homeless_by_coc",
           "Alias": "homeless_by_coc",
           "Startup Cost": 0.00,
           "Total Cost": 2363.61,
           "Plan Rows": 50686,
           "Plan Width": 0,
           "Actual Startup Time": 11.758,
           "Actual Total Time": 163.016,
           "Actual Rows": 50589,
           "Actual Loops": 1,
           "Filter": "(year > '2012-01-01'::date)",+
           "Rows Removed by Filter": 35940
         }
       ]
     },
     "Planning Time": 0.146,
     "Triggers": [
     ],
     "Execution Time": 305.343
   }
 ]

# ALTER, DELETE; need a rollback as it will really change the table
cur.execute("EXPLAIN (ANALYZE, format json) DELETE from state_info")
conn.rollback()



# INDEX ----------------
# An index creates a b-tree structure on a column, separate from the table, 
# which allows filtered queries to perform binary search. 
# Indexes reduce query speeds from O(n) complexity to O(logn)

# While creating indexes gives us tremendous speed benefits, 
# they come at the cost of space. Each index needs to be stored in the database file. 
# In addition, inserting, altering, and deleting rows takes longer since each of the affected indexes need to be updated. 
# Because indexes can be created after a table is created, 
# it's recommended to only create an index when you find yourself querying on a specific column frequently.

# create index
cur.execute('''
CREATE INDEX index_name ON table_name(column_name);
''')

# drop index
cur.execute('''
DROP INDEX IF EXISTS example_idx
''')

# multi-column index
cur.execute("""
CREATE INDEX state_year_idx ON homeless_by_coc(state, year)
""")
# ordering; faster read queries when constraining to a range (ie. WHERE count > 20)
'''CREATE INDEX example_idx ON example_table(col1, col2 DESC)'''

# partial index, restricting indexes on a subset of rows, e.g.:
'''CREATE INDEX example_range_idx ON example_table(col1) WHERE date_col > '2001-01-01';'''

# multi-column, partial index
cur.execute("CREATE INDEX state_year_measures_idx ON homeless_by_coc(state, lower(measures)) WHERE year > '2007-01-01'")



# PRIMARY KEYS ----------------
# primary keys are ultimately indexed
# if more than 1 primary key in a table, its called a composite key
cur.execute("""
CREATE TABLE state_idx (
    state CHAR(2),
    homeless_id INT,
    PRIMARY KEY (state, homeless_id) 
)
""")



# VACCUMING ----------------
# note that current versions of postgres are auto-vaccum
# check pg_stat_all_tables to find dead rows
"""
SELECT n_dead_tup 
FROM pg_stat_all_tables 
WHERE relname='homeless_by_coc'
"""
# | Column            | Type                     | Description                                                                      |
# |-------------------|--------------------------|----------------------------------------------------------------------------------|
# | relid             | oid                      | OID of a table                                                                   |
# | schemaname        | name                     | Name of the schema that this table is in                                         |
# | relname           | name                     | Name of this table                                                               |
# | seq_scan          | bigint                   | Number of sequential scans initiated on this table                               |
# | seq_tup_read      | bigint                   | Number of live rows fetched by sequential scans                                  |
# | idx_scan          | bigint                   | Number of index scans initiated on this table                                    |
# | idx_tup_fetch     | bigint                   | Number of live rows fetched by index scans                                       |
# | n_tup_ins         | bigint                   | Number of rows inserted                                                          |
# | n_tup_upd         | bigint                   | Number of rows updated                                                           |
# | n_tup_del         | bigint                   | Number of rows deleted                                                           |
# | n_tup_hot_upd     | bigint                   | Number of rows HOT updated (i.e., with no separate index update required)        |
# | n_live_tup        | bigint                   | Estimated number of live rows                                                    |
# | n_dead_tup        | bigint                   | Estimated number of dead rows                                                    |
# | last_vacuum       | timestamp with time zone | Last time at which this table was manually vacuumed (not counting VACUUM FULL)   |
# | last_autovacuum   | timestamp with time zone | Last time at which this table was vacuumed by the autovacuum daemon              |
# | last_analyze      | timestamp with time zone | Last time at which this table was manually analyzed                              |
# | last_autoanalyze  | timestamp with time zone | Last time at which this table was analyzed by the autovacuum daemon              |
# | vacuum_count      | bigint                   | Number of times this table has been manually vacuumed (not counting VACUUM FULL) |
# | autovacuum_count  | bigint                   | Number of times this table has been vacuumed by the autovacuum daemon            |
# | analyze_count     | bigint                   | Number of times this table has been manually analyzed                            |
# | autoanalyze_count | bigint                   | Number of times this table has been analyzed by the autovacuum daemon            |

# VACUUM, remove dead rows. must be uppercased
# need to set autocommit to True first
conn.autocommit = True
VACUUM homeless_by_coc

# rewrite explain analyze
cur.execute("VACUUM ANALYZE homeless_by_coc")

# like emptying recycling bin; will lock the table for edit, delete, insert; and slow down select
VACUUM FULL homless_by_coc



# SELECT ----------------
# select query
cur.execute('select * from notes)
# fetch all results from selection; returns list
notes = cur.fetchall()
# fetch first result form selection
one = cur.fetchone()




# CREATE TABLE ----------------
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS users")
cur.execute("""
        CREATE TABLE users(
            id INTEGER PRIMARY KEY,
            email text,
            name text,
            address text)
            """)
conn.commit()


# TEXT FIELDS
# char(20): not recommended, adds whitespace if text does not reach limit
# varchar(20): recommended if know max length
# text: recommended for uncertain sizes

# INTEGERS FIELDS
# | Name             | Storage Size | Description                     | Range                                                                                    |
# |------------------|--------------|---------------------------------|------------------------------------------------------------------------------------------|
# | smallint         | 2 bytes      | small-range integer             | -32768 to +32767                                                                         |
# | integer          | 4 bytes      | typical choice for integer      | -2147483648 to +2147483647                                                               |
# | bigint           | 8 bytes      | large-range integer             | -9223372036854775808 to 9223372036854775807                                              |

# DECIMAL FIELDS
# e.g., DECIMAL(3,2)
# PRECISION value which is the maximum amount of digits before AND/OR after the decimal point. 
# SCALE is the maximum amount of digits after the decimal number where scale must be less than or equal to precision. 

# | Name             | Storage Size | Description                     | Range                                                                                    |
# |------------------|--------------|---------------------------------|------------------------------------------------------------------------------------------|
# | decimal          | variable     | user-specified precision, exact | up to 131072 digits before the decimal point; up to 16383 digits after the decimal point |
# | numeric          | variable     | user-specified precision, exact | up to 131072 digits before the decimal point; up to 16383 digits after the decimal point |
# | real             | 4 bytes      | variable-precision, inexact     | 6 decimal digits precision                                                               |
# | double precision | 8 bytes      | variable-precision, inexact     | 15 decimal digits precision                                                              |
# | serial           | 4 bytes      | autoincrementing integer        | 1 to 2147483647                                                                          |
# | bigserial        | 8 bytes      | large autoincrementing integer  | 1 to 9223372036854775807                                                                 |

# DATETIME
# | Name                                    | Storage Size | Description                        | Low Value        | High Value      | Resolution                |
# |-----------------------------------------|--------------|------------------------------------|------------------|-----------------|---------------------------|
# | timestamp [ (p) ] [ without time zone ] | 8 bytes      | both date and time (no time zone)  | 4713 BC          | 294276 AD       | 1 microsecond / 14 digits |
# | timestamp [ (p) ] with time zone        | 8 bytes      | both date and time, with time zone | 4713 BC          | 294276 AD       | 1 microsecond / 14 digits |
# | date                                    | 4 bytes      | date (no time of day)              | 4713 BC          | 5874897 AD      | 1 day                     |
# | time [ (p) ] [ without time zone ]      | 8 bytes      | time of day (no date)              | 00:00:00         | 24:00:00        | 1 microsecond / 14 digits |
# | time [ (p) ] with time zone             | 12 bytes     | times of day only, with time zone  | 00:00:00+1459    | 24:00:00-1459   | 1 microsecond / 14 digits |
# | interval [ fields ] [ (p) ]             | 16 bytes     | time interval                      | -178000000 years | 178000000 years | 1 microsecond / 14 digits |



# COPY ----------------
with open('homeless_by_coc.csv') as f:
    cur.copy_expert('COPY homeless_by_coc FROM STDIN WITH CSV HEADER', f)
conn.commit()



# ALTER ----------------
# rename table
cur.execute('ALTER TABLE old_ign_reviews RENAME TO ign_reviews')
# drop column
cur.execute('ALTER TABLE table_name DROP COLUMN column_name')
# column type
cur.execute('ALTER TABLE table_name ALTER COLUMN column_name TYPE BIGINT')
# column name
cur.execute('ALTER TABLE table_name RENAME COLUMN old_col_nm TO new_col_nm')
# add new column
cur.execute('ALTER TABLE table_name ADD COLUMN column_name DATE')


# UPDATE ----------------
cur.execute("UPDATE ign_reviews SET release_date = to_date(release_day || '-' || release_month || '-' || release_year, 'DD-MM-YYYY')")
cur.execute("UPDATE fighter SET name=? WHERE url=?", (Fname, row[0]))
cur.execute("UPDATE fighter SET totalDraws=0 WHERE url=?", (row[0],)) # note comma must also be there if only one input



# LOAD WHOLE TABLE ----------------
# load whole csv into database table
import csv 
# copy_from does not work if there is additional comma in a single column
with open('ign.csv', 'r') as f:
    next(f) # skip header
    cur.copy_from(f, 'users', sep=',')

# alternative use copy_expert
with open('ign.csv', 'r') as f:
    cur.copy_expert('COPY ign_reviews FROM STDIN WITH CSV HEADER', f)



# INSERT & LOAD ----------------
# insert line by line
for line in reader:
    cur.execute("INSERT INTO users VALUES (%s,%s,%s,%s)",(line[0],line[1],line[2],line[3]))


f = open('user_accounts.csv', 'r')
next(f)
reader = csv.reader(f)
for line in reader:
    cur.execute("INSERT INTO users(id,email,name,address) VALUES (%s,%s,%s,%s)",(line[0],line[1],line[2],line[3]))
    # OR
    cur.execute("INSERT INTO ign_reviews VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",line)
        
conn.commit()        
users = cur.fetchall()
conn.close()

# insert using SQL
cur.execute('''
INSERT INTO new_comment_table (id, keywords, comment_text) 
SELECT id, keywords, comment FROM old_comment_table
''')



# DELETE ----------------
cur.execute("delete from users")



# ROLLBACK ----------------
# for edit, create and delete
try:
    # Throws "ERROR: current transaction is aborted"
    cur.execute("DROP TABLE does_not_exist")
except:
    # Rollback the transaction
    conn.rollback()