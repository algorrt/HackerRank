# Author : Rajanikant Tenguria

#!/bin/python

import sys

def birthdayCakeCandles(n, a):
    return a.count(max(a))
    # Complete this function

n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))
result = birthdayCakeCandles(n, a)
print(result)
