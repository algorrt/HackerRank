# Author : Rajanikant Tenguria

#!/bin/python

import sys


n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
height = map(int, raw_input().strip().split(' '))

if k<max(height): 
    print max(height)-k 
else: 
    print 0
