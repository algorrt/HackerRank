# Author : Rajanikant Tenguria

import sys,time,math

a=["Zero ","One ","Two ","Three ","Four ","Five ","Six ","Seven ","Eight ","Nine ","Ten ","Eleven ","Twelve ","Thirteen ","Fourteen ","Fifteen ","Sixteen ","Seventeen ","Eighteen ","Nineteen "]+[""]*980
b=["Twenty ","Thirty ","Forty ","Fifty ","Sixty ","Seventy ","Eighty ","Ninety "]
for i in range(len(b)):
	a[(i+2)*10]=b[i]
for i in range (2,10):
	for j in range(1,10):
		a[10*i+j]= b[i-2]+a[j]
b=["Hundred ","Thousand","Million","Billion"]
for i in range(1,10):
	for j in range(1,100):
		a[i*100+j]=a[i]+b[0]+a[j]
for i in range(1,10):
	a[i*100]=a[i]+b[0]
"""for i in range(len(a)):
	print a[i]"""

b=["Thousand","Million","Billion"]
n=int(raw_input())
for i in range(n):
	x=[]	
	m=int(raw_input())
	while m>0:
		h=m%1000
		x.append(h)
		m/=1000
	#print x
	for i in range(len(x)-1,-1,-1):
		if x[i]>0 and i>0:
			print a[x[i]]+b[i-1],
		elif x[i]>0 and i==0:
			print a[x[i]]
		else:
			continue
