# Author : Rajanikant Tenguria

#!/bin/python

import sys
import math

q = int(raw_input().strip())
for a0 in xrange(q):
    x,y,z = raw_input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]
    if abs(z-x)<abs(z-y):
        print "Cat A"
    if abs(z-x)>abs(z-y):
        print "Cat B"
    if abs(z-x)==abs(z-y):
        print "Mouse C"
