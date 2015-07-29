# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 20:26:20 2015

@author: caped_crusader
"""

def selection_sort(a):
    n=len(a)
    for i in range(0,n-1):
        imin = i
        for j in range(i+1,n):
            if(a[j]<a[imin]):
                imin = j
        temp = a[i]
        a[i] = [imin]
        a[imin] = temp
    
    return a 