from pyspark import SparkConf, SparkContext

#--------------
# set configuration & spark context object
conf = SparkConf().setMaster("local").setAppName("MinTemperatures")
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
swap = total.map(lambda x: (x[1],x[0])).sortByKey()

# look up from another RDD
mostPopularName = namesRdd.lookup(mostPopular[1])[0]

#--------------
# collect the results
results = words.collect()

#--------------
# broadcasting; send data to every node ahead of time
nameDict = sc.broadcast(loadMovieNames())
