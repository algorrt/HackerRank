"""
Author    : Rajanikant Tenguria        
Language  : Python 2
Problem   : https://www.hackerrank.com/challenges/cut-the-sticks/problem
Max Time  : 0.03s
% Success : 94.32 (76504/81108)
"""

n = int(raw_input().strip())                                      # no. of sticks
ar = map(int,raw_input().strip().split(' '))                      # length of sticks
m = 0
while m == 0:
    print len(ar)                                                 # current number of sticks
    mn = min(ar)                                                    # minimum length of stick
    ar = list(filter(lambda a: a != mn, ar))                        # updating the array of sticks
    if len(ar) == 0:
        m = 1       
