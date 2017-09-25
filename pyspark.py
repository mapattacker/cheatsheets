import findspark #pyspark can't be detected if file is at other folders than where it is installed
findspark.init()

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Basics").getOrCreate() #appName can be anything

## READING
#----------------------------
df = spark.read.json('people.json')
df.show()

df.head() #shows a list of row objects
# [Row(age=None, name='Michael'), Row(age=30, name='Andy')]


## SCHEMA
#--------------------------------------------------------
#changing the schema
from pyspark.sql.types import StructField,StringType,IntegerType,StructType
data_schema = [StructField("age", IntegerType(), True),StructField("name", StringType(), True)]
final_struc = StructType(fields=data_schema)
df = spark.read.json('people.json', schema=final_struc)

df.printSchema()


## EXPLORATORY
#--------------------------------------------------------
df.describe() #show datatypes
df.describe().show() #show max, min, stdev


## COLUMNS
#--------------------------------------------------------
df.columns #show column names
df.select('age').show() #have to use select to choose entire column
df.select(['age','name']).show() #multiple columns


# NEW COLUMNS
# Adding a new column with a simple copy
df.withColumn('newage',df['age']).show()
df.withColumn('add_one_age',df['age']+1).show() #with calculation


# RENAME COLUMN
df.withColumnRenamed('age','supernewage').show()



## SQL
#--------------------------------------------------------
# Register the DataFrame as a SQL temporary view
df.createOrReplaceTempView("people")
spark.sql("SELECT * FROM people WHERE age=30").show()




#--------------
# set configuration & spark context object
conf = SparkConf().setMaster("local").setAppName("MinTemperatures")
conf = SparkConf().setMaster("local[*]").setAppName("MovieSimilarities") #[*] use all cores in local computer
sc = SparkContext(conf = conf)


#--------------
# call the data from file and create RDD (Resilient Distributed Dataset)
lines = sc.textFile("file:///Users/Spark/1800.csv")


#--------------
### RDD MAPPING
parsedLines = lines.map(parseLine)  #use map function, output has same number of entries, just that it can be transformed.
words = input.flatMap(lambda x: x.split())  #use flat map function, output has more entries than input
# difference illustrated here: https://www.linkedin.com/pulse/difference-between-map-flatmap-transformations-spark-pyspark-pandey


#--------------
### RDD REDUCE
# key/value functions
  # reduce by key, x & y represent values of same key
total = parsedLines.reduceByKey(lambda x, y: x + y)
totalsByAge = rdd.mapValues(lambda x: (x, 1)).reduceByKey(lambda x, y: (x[0] + y[0], x[1] + y[1]))
  # swap key with value; and sort result by key
swap = total.map(lambda x: (x[1],x[0])).sortByKey() #or .sortByKey(ascending = False)

# top N results
.take(10)

# look up from another RDD
mostPopularName = namesRdd.lookup(mostPopular[1])[0]

#--------------
# collect the results
results = words.collect()

#--------------
# broadcasting; send data to every node ahead of time
nameDict = sc.broadcast(loadMovieNames())

#--------------
# partition; spark does not distribute on its own
  # for reduceByKey(), join(), lookup(), groupByKey(), etc.
.partitionBy(100)



#--------------
# SUBMIT IN CMD TO RUN SCRIPT
spark-submit script_name.py
spark-submit --executor-memory 1g MovieSimilarities1M.py 260  #change executor memory from default 512Mb to 1G
spark-submit --version #check spark version

# troubleshooting UI
# type localhost:4040 in browser when script is running. Open troubleshooting UI



