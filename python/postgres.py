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