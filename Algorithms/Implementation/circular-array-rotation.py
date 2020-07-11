# Author : Rajanikant Tenguria

#!/bin/python

import sys

n,k,q = map(int,raw_input().strip().split(' '))
a = map(int,raw_input().strip().split(' '))
mi=(n+k-1)%n
for a0 in xrange(q):
    m = int(raw_input().strip())    
    if m<mi:
        print a[n-mi+m-1]
    else:
print a[m-mi-1]
