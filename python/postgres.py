import psycopg2
conn = psycopg2.connect("dbname=dq user=sq password=eRqg123EEkl") #OR
conn = psycopg2.connect(dbname="dq", user="sq", password="eRqg123EEkl")
cur = conn.cursor()



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
cur.description



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




# COPY ----------------
with open('homeless_by_coc.csv') as f:
    cur.copy_expert('COPY homeless_by_coc FROM STDIN WITH CSV HEADER', f)
conn.commit()



# INSERT & LOAD ----------------
# insert line by line
for line in reader:
    cur.execute("INSERT INTO users VALUES (%s,%s,%s,%s)",(line[0],line[1],line[2],line[3]))

# load whole csv into database table
import csv 
f = open('user_accounts.csv', 'r')
next(f) # skip header
cur.copy_from(f, 'users', sep=',')
conn.commit()


cur.execute("UPDATE fighter SET name=? WHERE url=?", (Fname, row[0]))
cur.execute("UPDATE fighter SET totalDraws=0 WHERE url=?", (row[0],)) # note comma must also be there if only one input


cur.execute("delete from users")

f = open('user_accounts.csv', 'r')
reader = csv.reader(f)
for line in reader:
    if line[0] != 'id':
        cur.execute("INSERT INTO users(id,email,name,address) VALUES (%s,%s,%s,%s)",(line[0],line[1],line[2],line[3]))
        
conn.commit()        
users = cur.fetchall()
conn.close()