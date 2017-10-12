# APACHE AVRO

Avro is a a language-neutral file format used for serialising data in a json-like format. Avro requires a separate schema file to read together. 

It was developed by Doug Cutting, the founder of Hadoop. 

Read more: 
 * https://avro.apache.org/docs/current/gettingstartedpython.html
 * https://www.tutorialspoint.com/avro/avro_overview.htm
 * http://layer0.authentise.com/getting-started-with-avro-and-python-3.html

## Installation

`pip install avro`


## Schema File  (.avsc)

```
{"namespace": "example.avro",
 "type": "record",
 "name": "User",
 "fields": [
     {"name": "name", "type": "string"},
     {"name": "favorite_number",  "type": ["int", "null"]},
     {"name": "favorite_color", "type": ["string", "null"]}
 ]
}
```

## Avro File (.avro)

```
import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter

schema = avro.schema.parse(open("user.avsc", "rb").read())

writer = DataFileWriter(open("users.avro", "wb"), DatumWriter(), schema)
writer.append({"name": "Alyssa", "favorite_number": 256})
writer.append({"name": "Ben", "favorite_number": 7, "favorite_color": "red"})
writer.close()

reader = DataFileReader(open("users.avro", "rb"), DatumReader())
for user in reader:
    print user
reader.close()
```

## Reading & Writing Avro with Spark

`spark-submit --packages com.databricks:spark-avro_2.11:3.2.0 filename.py`

Read more: https://github.com/databricks/spark-avro

```
# Creates a DataFrame from a specified directory
df = spark.read.format("com.databricks.spark.avro").load("src/test/resources/episodes.avro")

#  Saves the subset of the Avro records read in
subset = df.where("doctor > 5")
subset.write.format("com.databricks.spark.avro").save("/tmp/output")
```

