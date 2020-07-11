
"""
Author    : Rajanikant Tenguria        
Language  : Python 2
Problem   : https://www.hackerrank.com/challenges/breaking-best-and-worst-records
Avg Time  : 0s
% Success : 98.60 (33095/33566)
"""

import sys
maxcnt = mincnt = 0
n = int(raw_input().strip())
s = map(int, raw_input().strip().split(' '))        # take input in an array
minimum = maximum = s[0]                            # initialize the min and max values
for i in range(1,n):                                # traverse through array
    if s[i] > maximum:
        maximum = s[i]
        maxcnt += 1                                 # if new element greater than max update max and counter
    if s[i] < minimum:
        minimum = s[i]
        mincnt += 1                                 # if new element less than min update max and counter
print maxcnt, mincnt                                
