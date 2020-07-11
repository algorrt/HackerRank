"""
Author    : Rajanikant Tenguria        
Language  : Python 2
Problem   : https://www.hackerrank.com/challenges/lisa-workbook/problem
Avg Time  : 0s
% Success : 90.38 (19297/21350)
"""

n,k = (int(x) for x in raw_input().split())                       # take no of chapters and no of problems per page
pages = map(int,raw_input().split())                              # no of pages in each chapter
page = 0
a = range(101)
cnt = 0
for i in range (n):
    chap_pages = pages[i]                                         # take pages of a particular chapter 
    next_page=1
    while(chap_pages>0):
        page += 1                                                 # increase no of pages while the problems keep on decreasing
        mn=min(chap_pages,k)
        #print a[next_page:next_page+mn]
        if page in a[next_page:next_page+mn]:                     # check if problem number and page number are same, if yes increase count 
            cnt += 1
        #print page,cnt
        next_page += k                                            # increase page
        chap_pages -= k                                           # decrease problems per chapter
print cnt                                                         # print count
