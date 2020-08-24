#!/bin/python3

import math
import os
import random
import re
import sys
import bisect


def median(x):
    lenx = len(x)
    if lenx % 2 == 0:
        return((x[lenx//2] + x[lenx//2 - 1])/2)
    if lenx % 2 != 0:
        return(x[lenx//2])

# Complete the activityNotifications function below.


def activityNotifications(expenditure, d):
    count = 0
    main = sorted(expenditure[:d])
    med = median(main)
    first = expenditure[0]
    for i in range(d, len(expenditure)+1):
        if expenditure[i] >= 2 * med:
            count += 1
        print(first, main, expenditure[i], med)
        main.remove(first)
        bisect.insort(main, expenditure[i])
        med = median(main)
        first = expenditure[i-d+1]

    return count


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    #fptr.write(str(result) + '\n')

    # fptr.close()
    print(result)
