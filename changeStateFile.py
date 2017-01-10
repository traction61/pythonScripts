#!/usr/bin/env python
import fileinput
import re

alpha = open("init/alpha.sludge", "r")
state = open("test.state", "rw")
for lineAlpha in alpha:
    alphaList = re.findall("value uniform ([0-9.]+)", lineAlpha)
    if len(alphaList) > 0:
        
        alphaNew = alphaList
    
        # open state file
        with open('test.state', 'r') as statefile :
            statefiledata = statefile.read()

        # replace the target string
        statefiledata = statefiledata.replace("alphaChange 3.122;", "alphaChange %s;" % alphaNew[0])

        # Write the statefile out again
        with open('test.state', 'w') as statefile:
            statefile.write(statefiledata)
alpha.close()
statefile.close()