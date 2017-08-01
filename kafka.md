### Basics
https://www.tutorialspoint.com/apache_kafka/apache_kafka_fundamentals.htm

There are 4 key components in Kafka.

__Producer__: Producers are the publisher of messages to one or more Kafka topics. Producers send data to Kafka brokers.

__Topics__: A stream of messages belonging to a particular category is called a topic. Data is stored in topics.

__Broker__: Brokers are simple system responsible for maintaining the published data.

__Consumer__: Consumers read data from brokers. Consumers subscribes to one or more topics and consume published messages by pulling data from the brokers.


### Installation

https://www.digitalocean.com/community/tutorials/how-to-install-apache-kafka-on-ubuntu-14-04

1. Install Java
2. Install Zookeeper
3. Extract Kafka Binaries
4. Configure & Start Kafka Server

  ``nohup ~/kafka/bin/kafka-server-start.sh ~/kafka/config/server.properties > ~/kafka/kafka.log 2>&1 &``
  
5. Test Kafka with a message from Broker to Consumer

  __Start a new topic called TutorialTopic__
  
  Enter some strings as messsages.
  ``bin/kafka-console-producer.sh --broker-list localhost:9092 --topic TutorialTopic``

  Or ask it to read from a file
  ``kafka-console-produce.sh --broker-list localhost:9092 --topic TutorialTopic --new-producer < my_file.txt``
    
  __Start Consumer in a new terminal to recieve messages__

  ``~/kafka/bin/kafka-console-consumer.sh --zookeeper localhost:2181 --topic TutorialTopic --from-beginning`` Messages should be received in this terminal 
  
6. Install KafkaT by Airbnb to manage Kafka


### Kafka & Python

https://scotch.io/tutorials/build-a-distributed-streaming-system-with-apache-kafka-and-python

https://github.com/dpkp/kafka-python

### Kafka-Manager

This is a Kafka manager created by Yahoo.

http://edbaker.weebly.com/blog/install-and-evaluation-of-yahoos-kafka-manager

It is necessary to install sbt as a prerequisite, which includes Scala.

http://edbaker.weebly.com/blog/install-and-evaluation-of-yahoos-kafka-manager

### Single File Stream

It is possible to have kafka monitor a single file for updates through filestream connector

http://docs.confluent.io/current/connect/connect-filestream/filestream_connector.html

### New Files Stream

This connector watch a directory for files and read the data as new files are written to the input directory.

https://github.com/jcustenborder/kafka-connect-spooldir