# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 12:37:18 2015

@author: caped_crusader
"""
class Stack:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
        
    def push(self,item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
        
    def peek(self):
        return self.items[len(self.items)-1]
        
    def size(self):
        return len(self.items)
        
def parChecker(symbolString):
    i = 0
    length = len(symbolString)
    balanced = True
    s = Stack()
    a = ["(","[","{"]
    while i<length and balanced:
        if symbolString[i] in a:
            s.push(symbolString[i])
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,symbolString[i]):
                    balanced = False
                
        i = i + 1
                
    if s.isEmpty() and balanced:
            return True
    else:
            return False
            
def matches(op,cl):
    opens = ["(","[","{"]
    closes = [")","]","}"]
    return opens.index(op) == closes.index(cl)
    
print(parChecker('{{([][])}()}'))
print(parChecker('[{()]'))
print(parChecker('{{([][)}())'))
    
    