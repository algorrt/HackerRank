# Author : Rajanikant Tenguria

import sys

m,n=map(int,raw_input().split())
f=map(int,raw_input().split())
for i in range(m):
    f[i]=f[i]%n
#print f
a=[0]*n
for i in range(m):
    a[f[i]]+=1
    #print a
out=0
if a[0]>0:
    out=1
#print out
if n%2==0:
    nn=n/2-1
    if a[nn/2]>0:
        out=out+1
    #print n
elif n%2!=0:
    nn=n/2
#print out  
for i in range(1,nn+1):
    if (a[i]>a[n-i]):
        out+=a[i]
    if (a[i]<=a[n-i]):
        out+=a[n-i]
    #print a,out,i,n-i
print out
