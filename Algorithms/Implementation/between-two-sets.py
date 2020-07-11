"""
Author    : Rajanikant Tenguria        
Language  : Python 2
Problem   : https://www.hackerrank.com/challenges/between-two-sets
Avg Time  : 0s
% Success : 88.15 (32162/36484)
"""

import sys
count=0
n, m = raw_input().strip().split(' ')
n, m = [int(n), int(m)]
a = map(int, raw_input().strip().split(' '))        # first array
b = map(int, raw_input().strip().split(' '))        # second array
b.sort()
mn=min(b)                                                  
for i in range (1,mn+1):                            # optimisation as less values re computed for 
    bool=1
    for j in range (len(b)):                        # traverse through second array
        if b[j]%i==0:
            for k in range (len(a)):                # if condiiton satisfied traverse through first array
                if i%a[k]==0:
                    bool*=1
                else:
                    bool=0
                    break
        else:
            bool=0
            break
    if bool==1:                                 # if all elements in array a satisfy the above condition bool return 1 and counter is increased
        count+=1
        #print i,b[j],a[k]
print count
