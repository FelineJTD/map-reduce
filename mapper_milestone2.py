#!/home/bigdata/anaconda3/bin/python
"""mapper.py"""

import sys

# input from STDIN
for line in sys.stdin:
    data = line.strip().split("\t")
    date, time, store, item, price, payment = data
    if (len(data) == 6) and ("Miami" in store or "San Francisco" in store or "Atlanta" in store):
        print("%s\t%s" % (store.strip(), price.strip()))