# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 14:56:28 2015

@author: caped_crusader
"""
def binary_search(a,n,value):
    if n==1:
        if a[0] == value:
            return True
        else:
            return False
    if value < a[n/2]:
        return binary_search(a[:n/2],len(a[:n/2]),value)
    elif value > a[n/2]:
        return binary_search(a[(n/2)+1:],len(a[(n/2)+1:]),value)
    elif value == a[n/2]:
        return True