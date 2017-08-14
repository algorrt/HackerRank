# Author : Rajanikant Tenguria

#!/bin/python

import sys

count=1
s = raw_input().strip()
for i in range(len(s)):
    if ord(s[i])<97:
        count+=1
print count
