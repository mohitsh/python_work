# -*- coding: utf-8 -*-
"""
Created on Sat Jul 04 22:37:39 2015

@author: caped_crusader
"""
def parChecker(s):
    s = list(s)
#    print "s ", s
    store = []
    n = len(s)
#    print "length", n
    if s[0] == ")" or s[0] == "]" or s[0] == "}":
        return False
    else:
        for i in range(n):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                store.append(s[i])
            elif s[i] == ")" or s[i] == "}" or s[i] == "]":
                store.pop()
    if store == []:
        return True
    else:
        return False
      
     
    
print parChecker('[ [ { { ( ( ) ) } } ] ]')
print parChecker('[ [ { { ( (  ) } } ] ]')
print parChecker('[')
print parChecker(']')
print parChecker('[]')



