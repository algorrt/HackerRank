# Author : Rajanikant Tenguria

import sys

n=int(raw_input())
a=map(int,raw_input().split())
h=[0]*(n+1)
for i in range (n+1):
    h[a[a[i-1]-1]]=i
for i in range(0,n):    
    print h[i+1]
