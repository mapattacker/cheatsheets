## Basics
https://www.tutorialspoint.com/apache_kafka/apache_kafka_fundamentals.htm

There are 4 key components in Kafka.

__Producer__: Producers are the publisher of messages to one or more Kafka topics. Producers send data to Kafka brokers.

__Topics__: A stream of messages belonging to a particular category is called a topic. Data is stored in topics.

__Broker__: Brokers are simple system responsible for maintaining the published data.

__Consumer__: Consumers read data from brokers. Consumers subscribes to one or more topics and consume published messages by pulling data from the brokers.


## Installation

https://www.digitalocean.com/community/tutorials/how-to-install-apache-kafka-on-ubuntu-14-04

1. Install Java
2. Install Zookeeper
3. Extract Kafka Binaries
4. Configure & Start Kafka Server

  `nohup ~/kafka/bin/kafka-server-start.sh ~/kafka/config/server.properties > ~/kafka/kafka.log 2>&1 &`
  
5. Test Kafka with a message from Broker to Consumer

  __Start a new topic called TutorialTopic__
  
  Enter some strings as messsages.
  `~/kafka/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic TutorialTopic`

  Or ask it to read from a file
  `kafka-console-produce.sh --broker-list localhost:9092 --topic TutorialTopic --new-producer < my_file.txt`
    
  __Start Consumer in a new terminal to recieve messages__

  `~/kafka/bin/kafka-console-consumer.sh --zookeeper localhost:2181 --topic TutorialTopic --from-beginning` Messages should be received in this terminal 
  
6. Install KafkaT by Airbnb to manage Kafka


## Kafka & Python

https://scotch.io/tutorials/build-a-distributed-streaming-system-with-apache-kafka-and-python

https://github.com/dpkp/kafka-python

## Kafka-Manager

1. This is a Kafka manager created by Yahoo.

    https://github.com/yahoo/kafka-manager

2. It is necessary to install sbt as a prerequisite, which includes Scala.

    http://edbaker.weebly.com/blog/install-and-evaluation-of-yahoos-kafka-manager

3. If there are issues with the `sbt clean dist`, look at reinstalling java (likely missing javac) by using the link below.

    https://www3.ntu.edu.sg/home/ehchua/programming/howto/JDK_Howto.html

4. Extract the created zip file to ~/. To start the kafka-manager
    * `cd kafka-manager-1.1*` go to extracted folder
    * `bin/kafka-manager` launch the server
    * Type `localhost:9000` in browser

## Single File Stream

It is possible to have kafka monitor a single file for updates through filestream connector

http://docs.confluent.io/current/connect/connect-filestream/filestream_connector.html

## New Files Stream

This connector watch a directory for files and read the data as new files are written to the input directory.

https://github.com/jcustenborder/kafka-connect-spooldir


## Python Kafka

`pip install kafka-python`

__Consumer__

```
from kafka import KafkaConsumer
consumer = KafkaConsumer("Tatooine", bootstrap_servers="192.168.0.2", auto_offset_reset='earliest', enable_auto_commit=False)

for msg in consumer:
    log = msg.value
    log = log.split('\n')
    for n, i in enumerate(log):
        print n, i
```

__Other Messages in Consumer__

```
for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))
```

__Get list of topics__

```
topic = "*"
consumer = KafkaConsumer(topic, bootstrap_servers="192.XXX.X.X", auto_offset_reset='earliest', enable_auto_commit=False)

print consumer.topics()
>>> set([u'z1', u'test_topic', u'Z1'])
```

## Kafka Spark-Streaming

Submit in command line. spark-streaming jar file will be downloaded to a local folder and will pull from it next time.
Remember to update kafka & spark version respectively for `2.10` & `1.6.1`.

`spark-submit --packages org.apache.spark:spark-streaming-kafka_2.10:1.6.1 kafka2spark.py`

Python script
```
from pyspark import SparkContext  
from pyspark.streaming import StreamingContext  
from pyspark.streaming.kafka import KafkaUtils

start = time.time()

# Spark Streaming
# ----------------------------------------
sc = SparkContext(appName="PythonSparkStreamingKafka_RM_01")  
sc.setLogLevel("WARN")
ssc = StreamingContext(sc, 1) # listen every 1 second
# ssc = spark-streaming context, zkQuorum = zookeeper, groupid = kafka topic group-id, topics = topicname:#partitions
kafkaStream = KafkaUtils.createStream(ssc=ssc, zkQuorum='192.168.0.2:2181', groupId='m1', topics={'m1':1}) 

parsed = kafkaStream.map(lambda x: x)  
parsed.pprint()

ssc.start()
ssc.awaitTermination()
```

# Spark Structured Streaming
# ----------------------------------------

https://spark.apache.org/docs/latest/structured-streaming-kafka-integration.html
https://databricks.com/blog/2017/04/26/processing-data-in-apache-kafka-with-structured-streaming-in-apache-spark-2-2.html
