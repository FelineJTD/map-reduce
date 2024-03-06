#!/home/bigdata/anaconda3/bin/python
"""mapper.py"""

import sys
from datetime import datetime, time

# input from STDIN
for line in sys.stdin:
    data = line.strip().split("\t")
    date, timedata, store, item, price, payment = data
    timestamp = datetime.strptime(timedata, "%H:%M").time()
    if (len(data) == 6):
        if (time(9,1) <= timestamp <= time(10, 0)):
            print("%s\t%s" % ("09:01-10:00", 1))
        elif (time(10,1) <= timestamp <= time(11, 0)):
            print("%s\t%s" % ("10:01-11:00", 1))