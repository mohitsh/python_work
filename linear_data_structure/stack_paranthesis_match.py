# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 01:56:56 2015

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
    s = Stack()
    i = 0
    length = len(symbolString)
    balanced = True
    while i < length and balanced:
        if symbolString[i] == "(":
            s.push("(")
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        i = i + 1
                
    if balanced and s.isEmpty():
        return True
    else:
        return False
    
print parChecker('((()))')       
print parChecker('((()))))))')   



""" simple implementation using a list """
def parChecker(parstr):
    inarray = []
    length = len(parstr)
    i = 0 
    balanced = True
    
    while i<length and balanced:
        if parstr[i] == "(":
            inarray.append("(")
        else:
            if len(inarray) == 0:
                balanced = False
            else:
                inarray.pop()
        i = i + 1
    
    if len(inarray) == 0 and balanced:
        return True
    else:
        return False
            

print parChecker('((()))')
print parChecker('(((()')