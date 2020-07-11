"""
# Author : Rajanikant Tenguria

Problem 003
There are two kangaroos on a number line ready to jump in the positive direction (i.e, toward positive infinity). 
The first kangaroo starts at location and moves at a rate of meters per jump. The second kangaroo starts at location and 
moves at a rate of meters per jump. Given the starting locations and movement rates for each kangaroo, can you determine 
if they'll ever land at the same location at the same time?

"""

x1, v1, x2, v2 = raw_input().strip().split(' ')                                          
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]                                # take input of positions and their velocities
if(x1<x2 and v1<v2):
    print "NO"
else:
    diff=x2-x1
    vdiff=v2-v1
    if(vdiff==0 and diff!=0):
        print "NO"
    else:
        if diff % vdiff==0:
            print "YES"
        else:
            print "NO"
