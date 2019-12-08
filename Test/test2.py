import numpy as np

def solution(A):
    # write your code in Python 3.6
    s = 0
    cum_sum = 0
    for ii in range(len(A)):
        cum_sum += A[ii]
        s += (cum_sum == (ii+1)*(ii+2)/2)
    return s

A = []