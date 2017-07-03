# Author : Rajanikant Tenguria

#!/bin/python

import sys
maxcnt=mincnt=0
n = int(raw_input().strip())
s = map(int, raw_input().strip().split(' '))
minimum=maximum=s[0]
for i in range(1,n):
    if s[i]>maximum:
        maximum=s[i]
        maxcnt+=1
    if s[i]<minimum:
        minimum=s[i]
        mincnt+=1   
print maxcnt, mincnt
