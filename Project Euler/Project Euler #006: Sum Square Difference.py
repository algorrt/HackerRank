import sys

n = int(raw_input())
for h in range(n):
    r = int(raw_input())
    sqOfSum = pow((r*(r+1)/2),2)
    sumOfSq = (r * (r + 1) * (2*r + 1)) / 6
    print sqOfSum - sumOfSq
