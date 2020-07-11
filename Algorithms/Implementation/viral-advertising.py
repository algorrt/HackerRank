# Author : Rajanikant Tenguria

import math
n=int(raw_input())
init=5
tot=0
for i in range (n):
    tot=tot+math.floor(init/2)
    init=math.floor(init/2)*3
print int(tot) 
