# Author : Rajanikant Tenguria

#!/bin/python

import sys

nm=10000000
n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))
for i in range(n):
    if a.count(a[i])>1:
        tmp=a[i]
        ind = [i for i, val in enumerate(a) if val == tmp]
        for i in range(len(ind)-1) :
            nm=min(nm,ind[i+1]-ind[i])
        #print ind,nm 
if nm==10000000:
    print -1
else:
    print nm
