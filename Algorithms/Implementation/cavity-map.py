# Author : Rajanikant Tenguria

#!/bin/python

import sys

n = int(raw_input().strip())
grid = [[0 for x in range(n)] for y in range(n)]
for i in xrange(n):
    grid_temp = str(raw_input().strip())
    grid_temp = list(grid_temp)
    for j in range(n):
        grid[i][j] = int(grid_temp[j])
for i in range(1,n-1):
    for j in range(1,n-1):
        mx = max(grid[i+1][j],grid[i-1][j],grid[i][j+1],grid[i][j-1])
        if mx < grid[i][j]:
            grid[i][j]="X"
            
for i in range(n):
    x=''      
    for j in range(n):
        x += str(grid[i][j])
    print x
#print grid
