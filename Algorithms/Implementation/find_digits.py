# Author : Rajanikant Tenguria

#!/bin/python

import sys

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    m=cur=count=0
    m=n
    while m>0:
        cur=m%10
        if cur!=0:
            if n%cur==0:
                count+=1
        m=m/10
    print count   
