# -*- coding: utf-8 -*-
"""
Created on Fri Jul 03 14:53:28 2015

@author: caped_crusader
"""

def anagram(a,b):
    na = len(a)
    nb = len(b)
    store = []
    if na == nb:
        for i in range(na):
#            if a[i] in b:
#                return a,b,True
            for j in range(nb):
                if a[i] == b[j]:
                    store.append(a[i])
                    break
                else:
                    pass
        if na == len(store):
            return True
        else:
            return False,len(store)
    else:
        return False
        
print anagram('aditya','jain')
print anagram('namit','mittal')
print anagram('ananana','ananana')
print anagram('anoanoano','onaonaona')
print anagram('shukla','shukla')
print anagram('shukla','shukla886')