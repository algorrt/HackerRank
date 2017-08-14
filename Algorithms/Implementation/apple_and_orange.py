#Author : Rajanikant Tenguria

"""
Sam's house has an apple tree and an orange tree that yield an abundance of fruit. The apple tree is to the left of his house, 
and the orange tree is to its right. You can assume the trees are located on a single point, where the apple tree is at point 
and the orange tree is at point. When a fruit falls from its tree, it lands units of distance from its tree of origin along the -axis. 
A negative value of means the fruit fell units to the tree's left, and a positive value of means it falls units to the tree's right.

Given the value of for apples and oranges, can you determine how many apples and oranges will fall on Sam's house 
(i.e., in the inclusive range )? Print the number of apples that fall on Sam's house as your first line of output, 
then print the number of oranges that fall on Sam's house as your second line of output.
"""

import sys
apc=0                                                  # apple count
orc=0                                                  # orange count
s,t = raw_input().strip().split(' ')                   
s,t = [int(s),int(t)]                                  # take co-ordinates of house and convert to int
a,b = raw_input().strip().split(' ')
a,b = [int(a),int(b)]                                  # co-ordinates of apple and orange trees
m,n = raw_input().strip().split(' ')
m,n = [int(m),int(n)]                                  # number of apples and oranges 
ap = map(int,raw_input().strip().split(' '))           # co-ordinates of apples
for i in xrange(m):
    ap[i]=ap[i]+a
    if ap[i]<=t and ap[i]>=s:                          # if any in range of the house
        apc+=1                                         # increase the  counter
ora = map(int,raw_input().strip().split(' '))          # co-ordinates of oranges
for i in xrange(n):
    ora[i]=ora[i]+b
    if ora[i]<=t and ora[i]>=s:                        # if any in range of the house
        orc+=1                                         # increase counter
print apc
print orc
