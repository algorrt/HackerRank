# Author: Rajanikant Tenguria

#!/bin/python

import sys

max=0
h = map(int, raw_input().strip().split(' '))
word = raw_input().strip()
for i in range (len(word)):
    n=ord(word[i])-97
    if h[n]>max:
        max=h[n]
print max*len(word)    
