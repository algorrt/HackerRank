# Author : Rajanikant Tenguria

import sys

cnt=0
s = raw_input().strip()
s = list(s)
ls = len(s)
ors = [0]*(26*ls+1)
mx = (26*ls+1)
i = 1 
last = s[0]
s[0] = ord(s[0])-96
ors[s[0]] = 1
while i<ls:
    h = s[i]
    if s[i] == last:
        s[i] = ord(s[i])+s[i-1]-96
        ors[s[i]] = 1
    else:
        s[i] = ord(s[i])-96
        ors[s[i]] = 1
    last = h
    i += 1
n = int(raw_input().strip())
for a0 in xrange(n):
    x = int(raw_input().strip())
    if x > mx:
        print "No"
    else:
        if ors[x] == 1:
            print "Yes"
        else:
            print "No"
