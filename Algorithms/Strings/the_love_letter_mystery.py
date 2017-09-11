# Author : Rajanikant Tenguria

#!/bin/python

import sys

def theLoveLetterMystery(s):
    ls = len(s)
    cnt = 0
    for i in range (ls/2):
        cnt += max(ord(s[i]),ord(s[-1-i])) - min(ord(s[i]),ord(s[-1-i]))
    return cnt    
        

q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    result = theLoveLetterMystery(s)
    print(result)
