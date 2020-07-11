"""
Author    : Rajanikant Tenguria        
Language  : Python 2
Problem   : https://www.hackerrank.com/challenges/the-birthday-bar
Avg Time  : 0s
% Success : 93.49 (23769/25423)
"""

import sys
tot = cnt = 0                                                       
n = int(raw_input().strip())                                        # no. of pieces of chocolate
s = map(int, raw_input().strip().split(' '))                        # integers on consecutive chocolate bars
d, m = raw_input().strip().split(' ')                               # number of bars and sum of integers on those bars.
d, m = [int(d), int(m)]
for i in range(m):                                                  # for 1st combination
    tot = tot + s[i]                                                
   
if tot == d:
    cnt += 1        
if n > 1:                                                           # do more combinations exist
    for i in range(m,n):
        tot = tot + s[i] - s[i-m]                                   # check for all possible combinations
        if tot == d:
            cnt += 1
        #print cnt
print cnt
