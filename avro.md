# APACHE AVRO

Avro is a file format used for serialising data in a json-like format. It requires a separate schema file to read together.

Read more: https://avro.apache.org/docs/current/gettingstartedpython.html

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

## Reading Avro with Spark

Read more: https://github.com/databricks/spark-avro

```
# Creates a DataFrame from a specified directory
df = spark.read.format("com.databricks.spark.avro").load("src/test/resources/episodes.avro")

#  Saves the subset of the Avro records read in
subset = df.where("doctor > 5")
subset.write.format("com.databricks.spark.avro").save("/tmp/output")
```

