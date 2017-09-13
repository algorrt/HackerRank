# Author : Rajanikant Tenguria

#!/bin/python

import sys

def anagram(s):
    o=[0]*26
    ls = len(s)
    if ls % 2 == 1:
        return -1
    else:
        s1 = s[:ls/2]
        s2 = s[ls/2:]
        for i in range(len(s1)):
            o[ord(s1[i])-97] += 1
            o[ord(s2[i])-97] -= 1
        #print o
        h = [i for i in o if i > 0]
        return sum(h)

q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    result = anagram(s)
    print(result)
