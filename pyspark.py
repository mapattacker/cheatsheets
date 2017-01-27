from pyspark import SparkConf, SparkContext


# set configuration & spark context object
conf = SparkConf().setMaster("local").setAppName("MinTemperatures")
sc = SparkContext(conf = conf)


# call the data from file and create RDD (Resilient Distributed Dataset)
lines = sc.textFile("file:///Users/Spark/1800.csv")
parsedLines = lines.map(parseLine)  #use map function, output has same number of entries, just that it can be transformed.
words = input.flatMap(lambda x: x.split())  #use flat map function, output has more entries than input
# split data into key/value or just values

parsedLines.countByValue()  #count values, give key & count value


# collect the results
results = words.collect()



