# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 17:00:36 2015

@author: caped_crusader
"""
"""
at each step largest value is selected and then placed at its proper position.
example:
[26,54,93,17,77,31,44,55,20] ==>
[26,54,20,17,77,31,44,55,93] ==>
[26,54,20,17,55,31,44,77,93] ==>
[26,54,20,17,44,31,55,77,93] ==>
[26,31,20,17,44,54,55,77,93] ==>
[26,17,20,31,44,54,55,77,93] ==>
[20,17,26,31,44,54,55,77,93] ==>
[17,20,26,31,44,54,55,77,93] ==>
"""
def selction_sort(a):
    for fillslot in range(len(a)-1,0,-1):
        posOfMax = 0
        for location in range(1,fillslot + 1):
            if a[location] > a[posOfMax]:
                posOfMax = location
            
        tmp = a[fillslot]
        a[fillslot] = a[posOfMax]
        a[posOfMax] = tmp
    
    return a
    

a = range(1001,990,-1)
print a
selction_sort(a)
print a