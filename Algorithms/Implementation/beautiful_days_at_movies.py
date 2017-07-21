# Author :Rajanikant Tenguria

import sys
def reverse(num):
    rev = 0
    while num > 0:
        rev = (10*rev) + num%10
        num //= 10
    return rev

h=map(int,raw_input().split())
m=count=0
for i in range(h[0],h[1]+1):
    m=reverse(i)
    if (i-m)%h[2]==0:
        count+=1
print count 
