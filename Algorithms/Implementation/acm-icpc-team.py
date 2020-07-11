# Author : Rajanikant Tenguria

#!/bin/python

import sys
from collections import Counter

n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
topic = []
t = mx=count = 0
for topic_i in xrange(n):
   t = int(raw_input().strip(),2)
   topic.append(t)
count=h=0
#print topic
for i in range(len(topic)):
    for j in range(i,len(topic)):
        if i!=j:
            h=bin(topic[i]|topic[j]).count('1')
            #print h,mx
            if h==mx:
                count+=1
            if h>mx:
                #print mx,count 
                mx=h
                count=0
                count+=1
                #print mx,count 
  
print mx
print count
