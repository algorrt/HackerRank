# Author : Rajanikant Tenguria

#!/bin/python

import sys

def funnyString(s):
    ls = len(s)
    s = list(s)
    cnt = 0 
    for i in range(ls):
        s[i] = ord(s[i])-96
    
    #print s
    for i in range(ls-1,0,-1):
        s[i]=abs(s[i]-s[i-1])
    s = s[1:]
    srev = s[::-1]
    #print s
    #print srev
    for j in range(ls-1):
        if s[j] == srev[j]:
            cnt = 1
        else:
            cnt=0
            break
        #print cnt    
    if cnt == 1:
        return "Funny"
    else:
        return "Not Funny"
    # Complete this function

q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    result = funnyString(s)
    print(result)
