# Author: Rajanikant Tenguria

#!/bin/python

import sys

def solve(a0, a1, a2, b0, b1, b2):
    ac=0
    bc=0
    if a0>b0:
        ac+=1
    if a0<b0:
        bc+=1
    if a1>b1:
        ac+=1
    if a1<b1:
        bc+=1
    if a2>b2:
        ac+=1
    if a2<b2:
        bc+=1    
    return ac,bc
    # Complete this function

a0, a1, a2 = raw_input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = raw_input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print " ".join(map(str, result))
