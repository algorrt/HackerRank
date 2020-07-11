# Author : Rajanikant Tenguria

#!/bin/python

import sys

n = int(raw_input().strip())
p = int(raw_input().strip())
if(n==p):
    print 0
else:
    if(p%2==0):
        print min(p/2,int(round(float(n-1-p)/2)))
    if(p%2!=0):
        print min((p-1)/2,int(round(float(n-p)/2)))  
