# Author : Rajanikant Tenguria

#!/bin/python

import sys

d1,m1,y1 = map(int,raw_input().split(' '))
d2,m2,y2 = map(int,raw_input().split(' '))
#print d1,d2,m1,m2,y1,y2
if y2==y1:
    if m1>m2:
        print (m1-m2)*500
    elif m1==m2 and d1>d2:
        print (d1-d2)*15
    else: 
        print 0
elif y2<y1:
    print 10000
else:
    print 0
