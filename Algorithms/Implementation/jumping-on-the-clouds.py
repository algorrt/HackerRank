# Author: Rajanikant Tenguria

#!/bin/python

import sys

count,pos,i=0,0,0
n = int(raw_input().strip())
c = map(int,raw_input().strip().split(' '))
c.append(1)
while i<n-1:
    pos=i
    #print pos,c[i+2]
    if c[i+2]==0:
        i=i+2
        #print i
    else:
        i+=1
    count+=1
    #print pos,count,i
print count    
