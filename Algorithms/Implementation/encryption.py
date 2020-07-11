# Author : Rajanikant Tenguria

#!/bin/python

import sys
from math import sqrt,ceil,floor

f=count=g=0
res=''
s = raw_input().strip()
f=len(s)
n=int(sqrt(f))
m=int(ceil(float(f)/n))
if n*(n+1)<=f:
    m-=1
    n+=1
#print n,m 
if m==n:
    g=1
n=max(m,n)
i=0   
while count< (f):
    #print i,m
    #print i,f,n,count,res
    if i>=f:
        res+=" "
        if g==1:
            i=(len(res))/n
        if g==0:
            i=int(round (float(len(res))/n))
        #print g,len(res),n,i,(len(res)/n)
    #print i,f,n,count,res,len(res),len(res)/n
    #print " "
    res+=s[i]
    i+=n
    count+=1
    
print res 
