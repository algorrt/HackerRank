# Author : Rajanikant Tenguria 

import sys

fs = raw_input().strip()
ss = raw_input().strip()

lf=len(fs)
ls=len(ss)
k = int(raw_input().strip())
if lf>ls:
    culprit=ls
    for i in range ( ls):
        if ss[i]!=fs[i]:
            culprit=i
            break
if ls>=lf:
    culprit=lf
    for i in range ( lf):   
        if fs[i]!=ss[i]:
            culprit=i
            break
#print culprit
if culprit==(ls or lf) :
    if k>=(2*ls or 2*lf) or (k-(max(lf,ls)-min(lf,ls)))%2==0:
        print "Yes"
    else:
        print "No"
else:
    f=(k-((lf-culprit)+(ls-culprit)))
    if k>lf+ls:
        f=2
    if f%2==0 and f>=0:
        print "Yes"
    else:
        print "No"
