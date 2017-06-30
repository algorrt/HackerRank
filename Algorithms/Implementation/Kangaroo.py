# Author : Rajanikant Tenguria

#!/bin/python

import sys

x1, v1, x2, v2 = raw_input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
if(x1<x2 and v1<v2):
    print "NO"
else:
    diff=x2-x1
    vdiff=v2-v1
    if(vdiff==0 and diff!=0):
        print "NO"
    else:
        if diff % vdiff==0:
            print "YES"
        else:
            print "NO"
