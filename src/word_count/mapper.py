#!/usr/bin/env python


import sys
import json

def get_stop_words():
    return []

try:
    for line in sys.stdin:
        json_dict = json.loads(line)
        file = str(json_dict['file'])
        content = str(json_dict['content'])
        for sw in get_stop_words():
            content = content.replace(sw, "")
        print("%s\t%d" % (file, content))
except Exception as e:
    with open('/home/michal/PycharmProjects/hadoop_project/src/tmp/log2.log', 'a') as file:
        file.write(str(e))
