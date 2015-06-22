# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 23:04:40 2015

@author: caped_crusader
"""

def bubble_sort(a):
    for k in range(1,len(a)):
        for i in range(0, len(a)-1):
            if(a[i]>a[i+1]):
                temp = a[i]
                a[i] = a[i+1]
                a[i+1] = temp
    return a