# Installation in Ubuntu

__Get python modules, Java, Scale__

 1. Install pip3 `sudo apt install python-pip3`
 2. Install jupyter notebook `pip3 install jupyter`
 3. `sudo apt-get update`
 4. Install java `sudo apt-get install default-jre`
 5. Check java is installed `java -version`
 6. Install scala `sudo apt-get install scala`
 7. Check scala is installed `scala -version`
 8. `sudo pip3 install py4j`
 
__Get Apache Spark__
 1. Go to https://spark.apache.org/downloads.html
 2. Download latest Spark version
 3. Cut and paste tgz file to home folder
 4. unzip file `sudo tar -zxvf spark-2.2.0-bin-hadoop2.7`

__Define Paths__
 1. `export SPARK_HOME='home/ubuntu/spark-2.2.0-bin-hadoop2.7'`
 2. `export PATH=$SPARK_HOME:$PATH`
 3. `export PYTHONPATH=$SPARK_HOME/python:$PYTHONPATH`
 4. `export PYSPARK_DRIVER_PYTHON="jupyter"`
 5. `export PYSPARK_DRIVER_PYTHON_OPTS="notebook"`
 6. `export PYSPARK_PYTHON=python3`

__Grant Permissions to essential Spark folders__
 1. `sudo chmod 777 spark-2.2.0-bin-hadoop2.7`
 2. `cd spark-2.2.0-bin-hadoop2.7`
 3. `sudo chmod 777 python`
 4. `cd python`
 5. `sudo chmod 777 pyspark`


# Access pyspark from any Directory

`pip3 install findspark`

In the script or python shell

```
# order script to find spark location
import findspark
findspark.init('/home/jake/spark/spark-2.2.0-bin-hadoop2.7')
import pyspark
```