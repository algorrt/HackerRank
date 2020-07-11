"""
Author    : Rajanikant Tenguria        
Language  : Python 2
Problem   : https://www.hackerrank.com/challenges/queens-attack-2
Avg Time  : 0.08s
% Success : 66.24 (3289/4965) 
"""

ff=bf=fb=bb=fx=bx=fy=by=1000000
sm=0
n,k = map(int,raw_input().split())                        # take value of chessboard side and no of obstacles
x,y = map(int,raw_input().split())                        # position of queen
#y,x=x,y
for a0 in range(k):
    x1,y1 = map(int,raw_input().split())                  # position of obstacles
    
    """
    Here we will divide the chessboard in 8 parts similar to co-ordinate system with queen being at co-ordinates (0,0) :
    1. first quadrant (+,+) 2. second quadrant (-,+) 3. third quadrant (-,-) 4.fourth quadrant (+,-)
    5. positive x axis (+x,0) 6. Negative x-axis (-x,0) 7. Positive y axis (0,+y) 8. Negative y axis (0,-y)
    """
    
    if y1>y and x1>x and abs(y-y1)==abs(x-x1):            # first quad
        if abs(y-y1)<ff:
            ff=(y1-y-1)
    elif y1<y and x1>x and abs(y-y1)==abs(x-x1):          # second quad
        if abs(y-y1)<bf:
            bf=(y-y1-1)       
    elif y1>y and x1<x and abs(y-y1)==abs(x-x1):          # third quad
        if abs(y-y1)<fb:
            fb=(y1-y-1)
    elif y1<y and x1<x and abs(y-y1)==abs(x-x1):          # fourth quad
        if abs(y-y1)<bb:
            bb=abs(y-y1-1)
    elif y1==y and x1<x:                                  # -ve x axis
        if (x-x1)<bx:
            bx=abs(x-x1-1)			
    elif x1==x and y1>y:                                  # +ve y axis
        if (y1-y)<fy:
            fy=abs(y1-y-1)
    elif x1==x and y1<y:                                  # -ve y axis
        if (y-y1)<by:
            by=abs(y-y1-1)
    elif y1==y and x1>x:                                  # +ve x axis
        if (x1-x)<fx:
            fx=abs(x1-x-1)  
    #print x,y,x1,y1
    #print ff,bf,fb,bb,fx,bx,fy,by
    
    
"""
The values are stored in an array and are checked with spaces to the end of the board. Then the minumum of the two are selected. Later sum 
is printed
"""

diagonal=[ff,bf,fb,bb,fx,bx,fy,by]
#print diagonal
for i in range(8):
	if diagonal[i]==1000000 and i==0:
		diagonal[i]=min(n-y,n-x)
	if diagonal[i]==1000000 and i==1:
		diagonal[i]=min(n-x,y-1)
	if diagonal[i]==1000000 and i==2:
		diagonal[i]=min(n-y,x-1)
	if diagonal[i]==1000000 and i==3:
		diagonal[i]=min(y-1,x-1)
	if diagonal[i]==1000000 and i==4:
		diagonal[i]=n-x
	if diagonal[i]==1000000 and i==5:
		diagonal[i]=x-1
	if diagonal[i]==1000000 and i==6:
		diagonal[i]=n-y	
	if diagonal[i]==1000000 and i==7:
		diagonal[i]=y-1
for i in range(8):
	sm+=diagonal[i]
print sm
