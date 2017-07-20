# Author : Rajanikant Tenguria

import sys
count=0
n, m = raw_input().strip().split(' ')
n, m = [int(n), int(m)]
a = map(int, raw_input().strip().split(' '))
b = map(int, raw_input().strip().split(' '))
b.sort()
mn=min(b)
for i in range (1,mn+1):
    bool=1
    for j in range (len(b)):
        if b[j]%i==0:
            for k in range (len(a)):
                if i%a[k]==0:
                    bool*=1
                else:
                    bool=0
                    break
        else:
            bool=0
            break
    if bool==1:
        count+=1
        #print i,b[j],a[k]
print count
