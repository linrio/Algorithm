# coding=utf-8
# Create by Lingfeng Lin

import numpy as np
import sys
sys.setrecursionlimit(100000)

def insertionsort(A):
    for j in range(len(A)):
        key = A[j]
        i = j-1
        while (i >= 0 and A[i] > key):
            A[i+1] = A[i]
            i=i-1
        A[i+1] = key
    return A

def mergesort(A, l, r):
    L = []
    R = []
    if l < r:
        m = (l+r)/2
        for i in range(l,m):
            L.append(A[i])
        for i in range(m,r):
            R.append(A[i])

        mergesort(A, l, m)
        mergesort(A, m, r)
        merge(A, L, R, l, r)

def merge(A, L, R, l, r):
    i = 0
    i = 0
    for k in range(l,r):
        if L[i] < R[j]:
            A[k] = L[i]
            i = i+1
        else:
            A[k] = R[j]
            j = j+1

A = [7,4,9,1,6,5,2,3,0]
A = insertionsort(A)
#B = mergesort(A, 0, len(A))
print 'insertionsort result:',A
#print 'mergesort:', B


