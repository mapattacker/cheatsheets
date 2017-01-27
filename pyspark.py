from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("MinTemperatures")
sc = SparkContext(conf = conf)

lines = sc.textFile("file:///Users/Spark/1800.csv")
parsedLines = lines.map(parseLine)
