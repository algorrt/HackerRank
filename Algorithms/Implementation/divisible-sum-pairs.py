"""
Author    : Rajanikant Tenguria        
Language  : Python 2
Problem   : https://www.hackerrank.com/challenges/divisible-sum-pairs
Avg Time  : 0s
% Success : 97.72 (75152/76902)
"""

import sys
cnt = 0 
n, k = raw_input().strip().split(' ')                             # take no of elements in array and number it should be divisible by.
n, k = [int(n), int(k)]
a = map(int, raw_input().strip().split(' '))
for i in range(n):
    for j in range(i+1,n):
        if (a[i] + a[j]) % k == 0:                                # if remainder == 0, it is divisible by k
            cnt +=     1                                          # increase counter 
print cnt                
