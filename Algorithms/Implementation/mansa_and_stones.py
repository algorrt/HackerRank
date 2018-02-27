"""
Author    : Rajanikant Tenguria        
Language  : Python 2
Problem   : https://www.hackerrank.com/challenges/strange-code/problem
Avg Time  : 0s
% Success : 76.75 (16041/20901)
"""

import sys

a = [3]
ar=[0,3,2,1]
mul = 3
t = int(raw_input())
i = 0
last = 0
while i < t:
    mul *= 2
    i = a[last]+mul
    a.append(i)
    last += 1

if t < 4:
    print ar[t]
else :
    print mul-(t-a[-2]-1)
