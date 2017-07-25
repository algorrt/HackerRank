# Author : Rajanikant Tenguria

#!/bin/python

import sys

add=temp=0
n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
c = map(int,raw_input().strip().split(' '))
temp+=k
temp%=n
if(c[temp]==1):
    add+=3
else:
    add+=1
while (temp%n!=0):
    temp+=k
    temp%=n
    if(c[temp]==1):
        add+=3
    else:
        add+=1
print 100-add
