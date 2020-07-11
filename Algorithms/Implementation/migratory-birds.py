# Author : Rajanikant Tenguria

#!/bin/python

import sys
a1=a2=a3=a4=a5=0
f=[0,0,0,0,0]
n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))
for i in range (n):
    if a[i]==1:
        f[0]+=1
    if a[i]==2:
        f[1]+=1
    if a[i]==3:
        f[2]+=1
    if a[i]==4:
        f[3]+=1
    if a[i]==5:
        f[4]+=1
minn=f.index(max(f))
print minn+1
