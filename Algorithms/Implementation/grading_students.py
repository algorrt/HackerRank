"""
Author : Rajanikant Tenguria

Question 001

HackerLand University has the following grading policy:

    Every student receives a grade in the inclusive range from 0 to 100.
    Any grade less than 40 is a failing grade.

Sam is a professor at the university and likes to round each student's grade according to these rules:

    If the difference between the grade and the next multiple of 5 is less than 3, round grade up to the next multiple of 5.
    If the value of is less than , no rounding occurs as the result will still be a failing grade.

For example grade = 84, will be rounded to 85 but 29 will not be rounded because the rounding would result in a number that is less than 40.

Given the initial value of grade for each of Sam's n students, write code to automate the rounding process. For each grade, 
round it according to the rules above and print the result on a new line.

"""

import sys
n = int(raw_input())                        # number of students

for i in xrange(n):
    grade = int(raw_input())                # grade of a particular student
    if(grade<38):
        print grade                         # if grade less than 38 print as it is
    else:
        if(grade%5>2):                      # for more than 38 round off to next multiple of 5
            print (grade/5+1)*5
        else:
            print grade
