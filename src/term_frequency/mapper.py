#!/usr/bin/env python


import sys
import json

try:
    for line in sys.stdin:
        json_dict = json.loads(line)
        # with open('/home/michal/PycharmProjects/hadoop_project/src/tmp/log2.log', 'a') as file:
        #     file.write(json_dict)

        content = json_dict['content']
        file = json_dict['file']
        all_terms = len(content)
        for s in (json_dict['content']).split():
            print("%s|%s\t%lf" % (file, s, 1/all_terms))
except Exception as e:
    with open('/home/michal/PycharmProjects/hadoop_project/src/tmp/log2.log', 'a') as file:
        file.write(str(e))
