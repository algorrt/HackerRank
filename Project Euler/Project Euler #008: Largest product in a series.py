#!/bin/python

import sys

t = int(raw_input().strip())
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = raw_input()
    mx=0
    h= list(num)
    for i in range(len(h)):
        h[i]=int(h[i])
    for i in range(len(h)-k):
        mul=1
        for j in range(i,i+k):
            mul*=h[j]
        if mul>mx:
            mx=mul
            #print j,mx
    print mx         
