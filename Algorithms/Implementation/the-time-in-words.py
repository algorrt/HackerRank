"""
Author : Rajanikant Tenguria

Problem 048

Given the time in numerals convert it into words.

"""

import sys


h = int(raw_input().strip())
m = int(raw_input().strip())
minutes=["0","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","quarter","sixteen","seventeen","eighteen","nineteen","twenty","twenty one","twenty two","twenty three","twenty four","twenty five","twenty six","twenty seven","twenty eight","twenty nine"]
hours=["0","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve"]
if m>30 and m!=45:
    print minutes[60-m]+" minutes to "+hours[h+1]
if m<30 and m!=0  and m!=15:
    print minutes[m]+" minutes past "+hours[h]    
if m==0:
    print hours[h]+" o' clock"
if m==30:
    print "half past "+hours[h]
if m==15:
    print minutes[15]+" past "+hours[h]
if m==45:
    print minutes[15]+" to "+hours[h+1]
