# Author : Rajanikant Tenguria

#!/bin/python

import sys

def twoStrings(s1, s2):
    if len(set(s1) & set(s2))>0:
        return "YES"
    else:
        return "NO"
    # Complete this function

q = int(raw_input().strip())
for a0 in xrange(q):
    s1 = raw_input().strip()
    s2 = raw_input().strip()
    result = twoStrings(s1, s2)
    print(result)
