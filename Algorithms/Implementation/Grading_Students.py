#!/bin/python

import sys


n = int(raw_input())

for i in xrange(n):
    grade = int(raw_input())
    if(grade<38):
        print grade
    else:
        if(grade%5>2):
            print (grade/5+1)*5
        else:
            print grade


