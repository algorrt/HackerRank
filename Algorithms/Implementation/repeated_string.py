# Author : Rajanikant Tenguria

#!/bin/python
import sys

s = raw_input().strip()
n = long(raw_input().strip())
count=0
h=[0]*len(s)
for i in range(len(s)):
    if s[i]=='a':
        count += 1
    h[i]=h[i]+count

#print h ,n%len(s),count,n/len(s)*count
if n%len(s)==0:
    print n/len(s)*count
else:
    print n/len(s)*count+ h[n%len(s)-1]
