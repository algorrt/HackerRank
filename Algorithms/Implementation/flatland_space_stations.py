# Author : Rajanikant Tenguria

#!/bin/python

import sys

mx=0
n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
cities = map(int,raw_input().strip().split(' '))
cities.sort()
#print cities
for i in range(m-1):
    x = cities[i+1] - cities[i]
    if x > mx:
        mx = x
mlx = n-1-cities[m-1]
mfx = cities[0]
#print mx,mlx,mfx
if mfx >= mx/2 or mlx >= mx/2:
    print max(mfx,mlx)
else:
    if mx % 2 == 0 :
        print mx/2
    else:
        if mx < 3:
            print 0
        else:
            print mx/2
