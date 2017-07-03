# Author : Rajanikant Tenguria

#!/bin/python

import sys
cnt=0
n, k = raw_input().strip().split(' ')
n, k = [int(n), int(k)]
a = map(int, raw_input().strip().split(' '))
for i in range(n):
    for j in range(i+1,n):
        if (a[i]+a[j])%k==0:
            cnt+=1
print cnt                
