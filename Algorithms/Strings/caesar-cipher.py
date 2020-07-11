# Author : Rajanikant Tenguria

n = int(raw_input().strip())
s = raw_input().strip()
k = int(raw_input().strip())

d = {}
for i in range(0, 26):
    d[chr(97 + i)] = chr(97 + (i + k) % 26)
for i in range(0, 26):
    d[chr(65 + i)] = chr(65 + (i + k) % 26)
    
ss = [d[i] if(i in d) else i for i in s]    
print ''.join(ss)
