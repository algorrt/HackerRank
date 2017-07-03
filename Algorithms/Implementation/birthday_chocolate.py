# Author : Rajanikant Tenguria

#!/bin/python

import sys
tot=cnt=0
n = int(raw_input().strip())
s = map(int, raw_input().strip().split(' '))
d, m = raw_input().strip().split(' ')
d, m = [int(d), int(m)]
for i in range(m):
    tot=tot+s[i]
   
if tot == d:
    cnt+=1        
if n>1:
    for i in range(m,n):
        tot=tot+s[i]-s[i-m]
        if tot == d:
            cnt+=1
        #print cnt
print cnt
