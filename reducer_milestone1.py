#!/home/bigdata/anaconda3/bin/python
"""reducer.py"""

import sys

salesTotal = 0
oldKey = None

for line in sys.stdin:
    data = line.strip().split("\t")
    
    if (len(data) != 2):
        continue
    thisKey, thisSale = data
    if (oldKey and oldKey != thisKey):
        print("%s\t%s" % (oldKey, salesTotal))
        salesTotal = 0
    oldKey = thisKey
    salesTotal += float(thisSale)
    
if oldKey != None:
    print("%s\t%s" % (oldKey, str(salesTotal)))