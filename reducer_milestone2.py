#!/home/bigdata/anaconda3/bin/python
"""reducer.py"""

import sys

salesMax = 0
oldKey = None

for line in sys.stdin:
    data = line.strip().split("\t")
    
    if (len(data) != 2):
        continue
    thisKey, thisSale = data
    if (oldKey and oldKey != thisKey):
        print("%s\t%s" % (oldKey, salesMax))
        salesMax = 0
    oldKey = thisKey
    if (salesMax < float(thisSale)):
        salesMax = float(thisSale)
    
if oldKey != None:
    print("%s\t%s" % (oldKey, salesMax))