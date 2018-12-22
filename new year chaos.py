#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    m=0
    i=len(q)-1
    while i>=0:
        y=q[i]-(i+1)
        if y>2:
            print('Too chaotic')
            z=1
            break
        for j in range(max(0,q[i]-2),i):
            if q[j]>q[i]:
                m+=1
                z=0
        i-=1
    if z!=1:
        print(m)
            

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
