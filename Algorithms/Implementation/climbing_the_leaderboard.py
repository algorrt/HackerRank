# Author : Rajanikant Tenguria

#!/bin/python

import sys
from bisect import bisect

n = int(raw_input())
score = map(int, raw_input().split())
k = int(raw_input())
alice = map(int, raw_input().split())
score = list(set(score))
score.sort()

y = len(score)
for i in xrange(k):
	print y - bisect(score, alice[i]) + 1
