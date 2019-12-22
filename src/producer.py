from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer

from os import listdir
from os.path import isfile, join

import time

# value_schema_str = """
# {
#   "type": "record",
#   "name": "myrecord",
#   "fields": [
#     {
#       "name": "f1",
#       "type": "string"
#     }
#   ]
# }
# """

value_schema_str = """
{
   "name": "myrecord",
   "type": "record",
   "fields" : [
     {
       "name" : "file",
       "type" : "string"
     },
     {
       "name" : "content",
       "type" : "string"
     }
   ]
}
"""

# value_schema = avro.loads(value_schema_str)
# key_schema = avro.loads(key_schema_str)
# value = {"f1": "value11"}
# key = {"name": "Key"}


# avroProducer = AvroProducer({
#     'bootstrap.servers': 'localhost:9092',
#     'schema.registry.url': 'http://localhost:8081'
#     }, default_value_schema=value_schema)


# avroProducer.produce(topic='test_hdfs2', value=value)
# avroProducer.flush()

def produce(file, content):
    value = {"file": file, "content": content}

    value_schema = avro.loads(value_schema_str)

    avro_producer = AvroProducer({
        'bootstrap.servers': 'localhost:9092',
        'schema.registry.url': 'http://localhost:8081'
        }, default_value_schema=value_schema)

    avro_producer.produce(topic='corpuses', value=value)

    avro_producer.flush()


files = [f for f in listdir("output2/part6/") if isfile(join("output2/part6/", f))]

for f in files:
    name = f.replace(".txt", '')
    try:
        with open('output2/part6/' + f, 'r') as content_file:
            content = content_file.read().replace("\n", " ")
            produce(name, content)
    except Exception as e:
        print(e)
        continue
    time.sleep(2)



# produce("test", "test")