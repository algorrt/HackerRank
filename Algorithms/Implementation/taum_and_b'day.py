# Author : Rajanikant Tenguria

#!/bin/python

import sys

t = int(raw_input().strip())
for a0 in xrange(t):
    b,w = raw_input().strip().split(' ')
    b,w = [long(b),long(w)]
    x,y,z = raw_input().strip().split(' ')
    x,y,z = [long(x),long(y),long(z)]
    mx=max(x,y)
    mn=min(x,y)
    if (mx-mn>z):
        if mn==x:
            nn=w
        else:
            nn=b
        print (mn*(b+w)+(z*nn))
    else:
        print (b*x+w*y)
