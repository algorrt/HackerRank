# Author : Rajanikant Tenguria

#!/bin/python

import sys

t = int(raw_input().strip())
for i in xrange(t):
    n, m, s = map(int,raw_input().strip().split(' '))
    print ((s - 1 +m - 1) % n) + 1
