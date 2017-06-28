# Author : Rajanikant Tenguria

#!/bin/python

import sys
m=0
n=0
a = map(int, raw_input().strip().split(' '))
m=min(a)
n=max(a)
a.remove(n)
print sum(a),sum(a)-m+n
