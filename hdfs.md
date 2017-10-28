## Hadoop File System Commands

`hdfs dfs`  --launch a series of help

`hdfs dfs -put path\of\os\directory path\of\hdfs\directory` --copy directory & contents from edge to hdfs data-node

`hdfs dfs -ls dir_name` --list all files and directories in dir_name

`hdfs dts -rm \dir_name\file_name`  --delete file

`hdfs dts -rm -r dir_name`  --delete 


## Impala Shell
Most usual database commands are valid in the impala shell. 
Default database is default; there is no need to specify this.

`impala-shell`  --launch impala shell

`create database database_name;` --create new database

`use database_name;` --switch database

`show database` --show list of databases

`invalidate metadata;`  --initialise database tables

`show tables;`  --show all tables

`drop table table_name;` --delete table