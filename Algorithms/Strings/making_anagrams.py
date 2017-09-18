# Author : Rajanikant Tenguria

#!/bin/python

import sys

s1 = raw_input().strip()
s2 = raw_input().strip()
cnt = 0
f = [0] * 26
l1 = len(s1)
l2 = len(s2)
for i in range(l1):
    f[ord(s1[i])-97] += 1
for i in range(l2):    
    f[ord(s2[i])-97] -= 1
for i in range(26):
    if f[i] != 0:
        cnt += abs(f[i])
print cnt        
