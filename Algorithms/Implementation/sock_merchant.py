# Author : Rajanikant Tenguria

#!/bin/python

import sys

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
ar.sort()
count=0
#print ar
for i in range (len(ar)-1):
    if ar[i]==ar[i+1]:
        count+=1
        ar[i]=ar[i]+101
        ar[i+1]=ar[i+1]+102
print count  
#print ar
