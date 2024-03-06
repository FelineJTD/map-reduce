#!/home/bigdata/anaconda3/bin/python
"""mapper.py"""

import sys

# input from STDIN
for line in sys.stdin:
    data = line.strip().split("\t")
    date, time, store, item, price, payment = data
    if (len(data) == 6) and ("Toys" in item or "Consumer Electronics" in item):
        print("%s\t%s" % (item.strip(), price.strip()))