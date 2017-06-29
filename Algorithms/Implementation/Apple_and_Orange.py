#Author : Rajanikant Tenguria

import sys
apc=0
orc=0
s,t = raw_input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = raw_input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = raw_input().strip().split(' ')
m,n = [int(m),int(n)]
ap = map(int,raw_input().strip().split(' '))
for i in xrange(m):
    ap[i]=ap[i]+a
    if ap[i]<=t and ap[i]>=s:
        apc+=1
ora = map(int,raw_input().strip().split(' '))
for i in xrange(n):
    ora[i]=ora[i]+b
    if ora[i]<=t and ora[i]>=s:
        orc+=1
print apc
print orc
