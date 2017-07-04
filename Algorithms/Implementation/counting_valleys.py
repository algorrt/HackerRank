#Author : Rajanikant Tenguria

n=int(raw_input())
h=raw_input()
u=d=count=0
for i in range(n):
    if h[i]=='U':
        u+=1
    if h[i]=='D':
        d+=1
    if u==d and h[i]=='U':
        count+=1
    #print count 
        
print count
