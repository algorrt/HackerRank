# Author : Rajanikant Tenguria

#!/bin/python

import sys

tot=temp=0
n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))
a.sort()
#a=[5,4,3,2,1]
me=max(a,key=a.count)

if me-1 in a:
    print a.count(me)+a.count(me-1)
else:
    print a.count(me)+a.count(me+1)
