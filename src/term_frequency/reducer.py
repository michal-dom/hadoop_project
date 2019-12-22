#!/usr/bin/env python

import sys

last_key = None
total_value = 0.0

for input_line in sys.stdin:
    input_line = input_line.strip()
    this_key, value = input_line.split("\t", 1)
    value = float(value)

    if last_key == this_key:
        total_value += value
    else:
        if last_key:
            print("%s\t%lf" % (last_key, total_value))
        running_total = value
        last_key = this_key

if last_key == this_key:
    print("%s\t%lf" % (last_key, total_value))

