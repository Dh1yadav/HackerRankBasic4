#!/bin/python3

import math
import os
import random
import re
import sys

def solve(s):
    s=s.casefold()
    for i in range(len(s)):
        if s[i].isalpha()==True and (s[i-1]==" " or i==0):
            s=s[:i]+s[i].upper()+s[i+1:]
    k=str(s)
    return k


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
