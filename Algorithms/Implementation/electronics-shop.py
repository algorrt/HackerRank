#!/bin/python

import sys

money=-1
s,n,m = raw_input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
kb = map(int, raw_input().strip().split(' '))
dr = map(int, raw_input().strip().split(' '))
#  The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
kb.sort()
dr.sort()
for i in range(n):
    for j in range(m):
        if kb[i]+dr[j]<=s and kb[i]+dr[j]>=money:
            money =kb[i]+dr[j]
            #print kb[i],dr[j],money
print money
