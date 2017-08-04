https://www.tutorialspoint.com/mongodb/mongodb_overview.htm

# IDE

Robo 3T

# Basics

. No schema needs to be defined.
. Very fast to build a database because of that.
. JSON format
. New query language, with chained functions, learning curve low
. Has horizontal scaling through Sharing: storing records in multiple machines

`use dbname`  --select database, or create if not exist

`db`  --show current selected db

`db.stats()`  --show mongo server status

`show dbs`  --show available databases; db will not show if there are no documents in it

`db.movie.insert({"name":"tutorials point"})` --insert document called movie

`db.dropDatabase()` --drop database