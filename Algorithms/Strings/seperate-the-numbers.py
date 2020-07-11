# Author : Rajanikant Tenguria

#!/bin/python

import sys
    
q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    if len(s)>1 and s[0]!='0':
        for i in range(1,len(s)/2+1):
            h=int(s[:i])
            #print h
            nstr=str(h)+str(h+1)
            #print h,str(h),str(h+1),nstr,s[:len(nstr)]
            if nstr==s[:len(nstr)]:
                count=1
                #print h
                cnt=int(h)+1
                #print cnt
                nstr=str(nstr)
                #print cnt
                while len(nstr) < len(s) :
                    nstr+=str(int(cnt)+1)
                    cnt+=1
                if nstr==s:
                    break
                
        #print nstr,s
        if nstr==s:
            print "YES",h
        else:
            print "NO"
        #print a    
    else:
        print "NO"
