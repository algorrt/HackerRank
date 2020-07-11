# Author : Rajanikant Tenguria

#!/bin/python

import sys
t = int(raw_input().strip())
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    arr = map(int,raw_input().strip().split(' '))
    count = 0
    for i in arr:
        if i<=0:
            count += 1
    if count < k:
        print "YES"
    else:
        print "NO"
