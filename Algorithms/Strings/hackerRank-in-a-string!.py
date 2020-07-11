# Author : Rajanikant Tenguria

#!/bin/python

import sys

def check(s):
    cnt=0
    for i in range(len(s)):
        if s[i]==t[cnt]:
            cnt+=1
        if cnt ==9:
            break
    if cnt ==9:
        return "YES"
    else:
        return"NO"

t="hackerrank"    
q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    print check(s)
