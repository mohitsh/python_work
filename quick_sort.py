# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 01:59:22 2015

@author: caped_crusader
"""
def partition(a,start,end):
    pivot = a[end]
    pindex = start
    for i in range(start,n):
        if a[i] < pindex:
            temp = a[i]
            a[i] = a[i+1]
            a[i+1] = temp
            pindex = pindex + 1 
    temp = a[end]
    a[end] = a[pindex]
    a[pindex] = temp
    return pindex

def quick_sort(a,start,end):
    if start>=end:
        pindex = partition(a,start,end) #index of pivot
        quick_sort(a,start,pindex-1)
        quick_sort(a,pindex+1,end)
    return a
