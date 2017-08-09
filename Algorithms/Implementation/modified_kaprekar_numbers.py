# Author : Rajanikant Tenguria

def kapnum(i):
    f=len(list(str(i)))
    mod=10**(f)
    l=i*i
    j=l/mod
    k=l%mod
    #print i,j,k,j+k,l
    if (j+k)==i:
        return 1
    else:
        return 0

n=int(raw_input())
m=int(raw_input())
cnt=0
for i in range(n,m+1):
    if kapnum(i):
        print i,
        cnt+=1
if cnt==0:
    print "INVALID RANGE"
