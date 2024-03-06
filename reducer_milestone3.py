#!/home/bigdata/anaconda3/bin/python
"""reducer.py"""

import sys

salesCount = 0
oldKey = None

for line in sys.stdin:
    data = line.strip().split("\t")
    
    if (len(data) != 2):
        continue
    thisKey, thisSale = data
    if (oldKey and oldKey != thisKey):
        print("%s\t%s" % (oldKey, salesCount))
        salesCount = 0
    oldKey = thisKey
    salesCount += 1
    
if oldKey != None:
    print("%s\t%s" % (oldKey, salesCount))