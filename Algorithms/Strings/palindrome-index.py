# Author : Rajanikant Tenguria

#!/bin/python

import sys

def palindromeIndex(s):
    ls = len(s)
    h = []
    x = 0
    for i in range(ls/2):
        if s[i] != s[-1-i]:
            #print s, s[i],s[-i-1],s[-1-i-1]
            if x == 1:
                break
            else:
                #print s[i+1] , s[-1-i]
                if s[i+1:i+3] == s[-2-i:-i][::-1]:
                    h.append(i)
                    s = s[:i] + s[(i+1):]
                    #print "x"
                    x = 2
                elif s[i:i+2] == s[-3-i:-1-i][::-1]:
                    #print s[i:i+3] ,s[-4-i:-1-i][::-1]
                    h.append(ls-1-i)
                    s = s[:-i-1] + s[-i:]
                    #print "y"
                    x = 2
                else:
                    x = 1
                    break
            #print s, s[i],s[-i-1],s[-1-i-1]       
    #print h,s
    if len(h) == 0 or x == 1 or ls > len(s)+1 :
        return -1
    
    else: 
        return h[0]
    # Complete this function

q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    result = palindromeIndex(s)
    print(result)
