#!/usr/bin/env python

import avro
from avro.datafile import DataFileReader
from avro.io import DatumReader
import os
import sys

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


schema = avro.schema.Parse(value_schema_str)
# os.remove("test.avro")

data = sys.stdin.buffer.read()

with open('test.avro', 'wb') as file:
    file.write(data)


reader = DataFileReader(open("test.avro", "rb"), DatumReader())
for record in reader:
    name = record['file']
    content = str(record['content']).strip().split()
    for key in content:
        value = 1
        print("%s\t%d" % (key, value))
reader.close()

