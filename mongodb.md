https://www.tutorialspoint.com/mongodb/mongodb_overview.htm

# IDE

Robo 3T

# Basics

. No schema needs to be defined.
. Very fast to build a database because of that.
. JSON format
. New query language, with chained functions, learning curve low
. Has horizontal scaling through Sharing: storing records in multiple machines

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

Note that it is not necessary to create a collection. 
It will be automatically created when inserting a document.

```db.createCollection("mycol", { capped : true, autoIndexId : true, size :`
   `6142800, max : 10000 } )``` --create collection with properties

`db.COLLECTION_NAME.drop()` --drop collection

# Documents

`db.COLLECTION_NAME.insert(document)` --inserting a document

Object ID, if not specified, will be automatically entered with the following format:
`_id: ObjectId(4 bytes timestamp, 3 bytes machine id, 2 bytes process id, 3 bytes incrementer)` --unique id

```db.post.insert([
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
])```