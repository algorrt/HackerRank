# Author : Rajanikant Tenguria

from math import log

a=[1,2,3,4,5,6,7,8,9]
ln,base=(int(x) for x in (raw_input().split()))
n=len(str(ln))
#print n
x=range(1000)
def palindrome_generator(n):
	for i in range(2,n+1):
		if i%2==0:
			for j in range(pow(10,i/2-1),pow(10,i/2)):
				h=str(x[j])
				a.append(h+h[::-1])
		else:
			i=i-1
			up=pow(10,i/2)
			for j in range(pow(10,i/2-1),pow(10,i/2)):
				h=str(x[j])
				for k in range(0,10):
					z=h+str(k)+h[::-1]
					a.append(z)

	for i in range(len(a)):
		a[i]=int(a[i])

def base_converter(num,base):
	pivot=0
	bnum=''
	#print num
	val=[1]+[0]*int(log(num,base))
	for i in range(int(log(num,base))+1):
		val[i]=int(pow(base,i))
		if num<val[i]:
			pivot=i
			break
	pivot=i
	while(num>0):
		quo=0
		pw=int(pow(base,pivot))
		quo=num/pw
		pivot-=1
		num=num-quo*pw
		bnum+=str(quo)
	pivot=i
	#print pivot,bnum,len(bnum)
	if len(bnum)<pivot+1:
		for i in range(pivot+1-len(bnum)):
			bnum+='0'	
	#print bnum		
	rnum=bnum[::-1]
	#print rnum
	if rnum[:len(rnum)/2]==bnum[:len(rnum)/2]:
		#print bnum,rnum
		return 1
	else:
		return 0
		
sm=0	
res=[]
palindrome_generator(n)
#print a
for i in range(len(a)):
	bool=base_converter(a[i],base)
	if bool:
		res.append(a[i])
i=0
res.append(100000000)
while (res[i]<=ln):
	sm+=res[i]
	i+=1
print sm
#print res
