# Author : Rajanikant Tenguria

#!/bin/python

import sys

ave=0
n, k = raw_input().strip().split(' ')
n, k = [int(n), int(k)]
ar = map(int, raw_input().strip().split(' '))
x=ar[k]/2
b = int(raw_input().strip())
ar.remove(ar[k])
#print ar
#print sum(ar)/(n-1)
if sum(ar)/2==b:
    print "Bon Appetit"
else:
    print x
