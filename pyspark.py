from pyspark import SparkConf, SparkContext

#--------------
# set configuration & spark context object
conf = SparkConf().setMaster("local").setAppName("MinTemperatures")
conf = SparkConf().setMaster("local[*]").setAppName("MovieSimilarities") #use all cores in local computer
sc = SparkContext(conf = conf)

#--------------
# call the data from file and create RDD (Resilient Distributed Dataset)
lines = sc.textFile("file:///Users/Spark/1800.csv")
parsedLines = lines.map(parseLine)  #use map function, output has same number of entries, just that it can be transformed.
words = input.flatMap(lambda x: x.split())  #use flat map function, output has more entries than input

#--------------
### FUNCTIONS
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

# submit to run
spark-submit script_name.py
spark-submit --executor-memory 1g MovieSimilarities1M.py 260  #change executor memory from default 512Mb to 1G

# troubleshooting UI
# type localhost:4040 in browser when script is running. Open troubleshooting UI

#--------------
# breadth first search alogrithm
  # set each node with > list of friends, distance, flag
  # start with distance 0 for starting node and change flag
  # iterate and expand to adjacent nodes and change distance to 1 and change flag
  # continue till friend is found and obtain the distance
