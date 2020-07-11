# Author : Rajanikant Tenguria

#!/bin/python

from collections import *
import sys

s = raw_input().strip()
f = [0] * 26
ls = len(s)
for i in range(ls):
    f[ord(s[i])-97] += 1
    f[ord(s[i])-97] %= 2
h = Counter(f)
if h[1] > 1:
    print "NO"
else:
    print "YES"
