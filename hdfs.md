## Hadoop File System Commands

`hdfs dfs`  --launch a series of help

`hdfs dfs -put path\of\os\directory path\of\hdfs\directory` --copy directory & contents from edge to hdfs data-node

`hdfs dfs -get path\of\hdfs\directory path\of\os\directory` --copy directory & contents from hdfs data-node to edge

`hdfs dfs -ls dir_name` --list all files and directories in dir_name

`hdfs dfs -rm \dir_name\file_name`  --delete file

`hdfs dfs -rm -r dir_name`  --delete 


## Impala Shell
Most usual database commands are valid in the impala shell. 
Default database is default; there is no need to specify this.

`impala-shell`  --launch impala shell

`connect 192.168.xxx.xxx:21000;`  --connect to impala in the data-node

`create database database_name;` --create new database

`use database_name;` --switch database

`show database` --show list of databases

`invalidate metadata;`  --initialise database tables

`show tables;`  --show all tables

`drop table table_name;` --delete table