# Author : Rajanikant Tenguria

#!/bin/python

import sys

Q = int(raw_input().strip())
for a0 in xrange(Q):
    cnt=0
    ar=[0]*26
    x = 1
    n = int(raw_input().strip())
    b = raw_input().strip()
    i = 0
    b=list(b)
    while i < (len(b)-2):
        if b[i] == b[i+1] or b[i] == b[i-1]:
            x *= 1
            i += 1  
        else:
            x=0
            break
        i += 1 
    #print x
    empty = b.count("_")
    #print empty
    for i in range(len(b)):
        tmp = ord(b[i])-65
        if tmp < 27 :
            ar[ord(b[i])-65] += 1
    for i in range(26):
        if ar[i] == 1:
            cnt += 1
            break
    if cnt > 0:
        print "NO"
    else:
        if empty > 0:
            print "YES"
        else:
            if x == 1:
                print "YES"
            else:
                print "NO"
    #print ar
