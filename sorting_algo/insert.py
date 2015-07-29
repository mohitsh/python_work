# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def insert_sort(a):
    for i in range(1,len(a)):
        value = a[i]
        hole = i
        while hole > 0 and a[hole-1] > value:
            a[hole] = a[hole-1]
            hole = hole-1
        a[hole] = value
        
    return a