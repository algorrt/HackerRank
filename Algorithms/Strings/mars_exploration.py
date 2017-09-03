# Author : Rajanikant Tenguria

#!/bin/python

import sys
cnt=0
s = raw_input().strip()
for i in range(0,len(s),3):
    if s[i]!="S":
        #print i,s[i]
        cnt+=1
    if s[i+1]!="O":
        #print i+1,s[i+1]
        cnt+=1
    if s[i+2]!="S":
        #print i+2,s[i+2]
        cnt+=1    
print cnt        
