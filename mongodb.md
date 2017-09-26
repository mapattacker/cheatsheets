### MongoDB Tutorial
https://www.tutorialspoint.com/mongodb/mongodb_overview.htm
### Python Client
http://api.mongodb.com/python/current/tutorial.html


# IDE

Robo 3T

# Basics

 * No schema needs to be defined.
 * Very fast to build a database because of that.
 * JSON format
 * New query language, with chained functions, learning curve low
 * Has horizontal scaling through Sharing: storing records in multiple machines
 * mongod is the database server 
 * mongo is the command line for typing queries 

# Set-up

 * Setup windows environment variable for mongo server path "C:\Program Files\MongoDB\Server\3.4\bin"
 * Go control panel > System & Security > System > Advanced system settings > Environment Variables > User variables
 * Open cmd and type "mongod" to start mongodb server
 * Create folders data & within it, db * This stores the databases "C:\data\db"
 * Now you can start playing with it


# Database

`use dbname`  --select database, or create if not exist

`db`  --show current selected db

`db.stats()`  --show mongo server status

`show dbs`  --show available databases; db will not show if there are no documents in it

`db.movie.insert({"name":"tutorials point"})` --insert collection called movie, with the document content

`db.dropDatabase()` --drop database

# Collections

Collections act like tables in an RDBMS.

`show collections`  --show collections 

Note that it is not necessary to create a collection * 
It will be automatically created when inserting a document.

```db.createCollection("mycol", { capped : true, autoIndexId : true, size :`
   `6142800, max : 10000 } )``` --create collection with properties

`db.COLLECTION_NAME.drop()` --drop collection

# Documents

`db.COLLECTION_NAME.insert(document)` --inserting a document

Object ID, if not specified, will be automatically entered with the following format:
`_id: ObjectId(4 bytes timestamp, 3 bytes machine id, 2 bytes process id, 3 bytes incrementer)` --unique id

```
db.post.insert([
 {
    title: 'MongoDB Overview', 
    description: 'MongoDB is no sql database',
    by: 'tutorials point',
    url: 'http://www.tutorialspoint.com',
    tags: ['mongodb', 'database', 'NoSQL'],
    likes: 100
 },

 {
    title: 'NoSQL Database', 
    description: 'NoSQL database doesn't have tables',
    by: 'tutorials point',
    url: 'http://www.tutorialspoint.com',
    tags: ['mongodb', 'database', 'NoSQL'],
    likes: 20, 
    comments: [	
       {
          user:'user1',
          message: 'My first comment',
          dateCreated: new Date(2013,11,10,2,35),
          like: 0 
       }
    ]
 }
])
```

# Query (WHERE clause)

`db.mycol.find()`

use pretty printing

`db.mycol.find().pretty()` --use pretty printing

```
db.mycol.find({"likes": {$gt:10}, $or: [{"by": "tutorials point"},
{"title": "MongoDB Overview"}]}).pretty()
```
--where likes>10 AND (by = 'tutorials point' OR title = 'MongoDB Overview')


# Query (LIMIT clause)

`db.COLLECTION_NAME.find().limit(NUMBER)` --limit by

`db.COLLECTION_NAME.find().limit(NUMBER).skip(NUMBER)`  --skip by # rows


# Explain

```
db.collection.find(query).explain()
{
    // BasicCursor means no index used, BtreeCursor would mean this is an indexed query
    "cursor" : "BasicCursor",
    
    // The bounds of the index that were used, see how much of the index is being scanned
    "indexBounds" : [ ],
    
    // Number of documents or indexes scanned
    "nscanned" : 57594,
    
    // Number of documents scanned
    "nscannedObjects" : 57594,
    
    // The number of times the read/write lock was yielded
    "nYields" : 2 ,
    
    // Number of documents matched
    "n" : 3 ,
    
    // Duration in milliseconds
    "millis" : 108,
    
    // True if the results can be returned using only the index
    "indexOnly" : false,
    
    // If true, a multikey index was used
    "isMultiKey" : false
}
```

# Export as CSV

In Mongo Shell

`mongoexport --db wsg-database --collection wsg --type=csv --fieldFile fields.txt --out export.csv`

In Python
```
import pymongo
import subprocess

subprocess.call(r'mongoexport --db wsg-database --collection wsg --type=csv --fieldFile "C:\Users\Teo XXX\Desktop\fields.txt" --out "C:\Users\Teo XXX\Desktop\export.csv"', shell=True)
subprocess.call(["mongoexport", "--db", "mydb", "--collection", "url_db","--type=csv", "--fieldFile", "fields.txt", "--out ", export.csv])
```


In Python
```
# get unique fields from mongodb
fields = []
for i in db['wsg'].find({}):
    test.extend(i.keys())

fields = list(set(test))
# remove mongodb unique id
fields.remove('_id')
fields


# proper format for exporting as a field name txt field for mongoexport
with open(r'C:\Users\Teo XXX\Desktop\fields.txt', 'w') as file:
    for i in test:
        file.write(i + '\n')
```

# Spark-MongoDB Connector 
https://docs.mongodb.com/spark-connector/master/python-api/

Download the jar file of the connector. Place in `C:\spark\jars` folder.

Use `spark-submit --jars C:/spark/jars/mongo-spark-connector_2.10-2.2.0.jar filename.py`

```
from pyspark.sql import SparkSession


spark = SparkSession \
    .builder \
    .appName("myApp") \
    .config("spark.mongodb.input.uri", "mongodb://localhost:27017/wsg-database.wsg") \
    .config("spark.mongodb.output.uri", "mongodb://localhost:27017/wsg-database.wsg") \
    .getOrCreate()


df = spark.read.format("com.mongodb.spark.sql.DefaultSource").load()
df.printSchema()
```