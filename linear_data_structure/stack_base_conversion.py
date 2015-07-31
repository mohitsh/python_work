# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 13:38:38 2015

@author: caped_crusader
"""

class Stack:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
        
    def size(self):
        return len(self.items)
        
    def push(self,item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
        
    def peek(self):
        return self.items[len(self.items)-1]
        
    
def baseConversion(num,base):
    s = Stack()
    digits = "0123456789ABCDEF"
    while num >= 1:
        s.push(num%base)
        num = num//base
    
    converted = ''
    while not s.isEmpty():
        converted = converted + digits[s.pop()]
        
    return converted
    
print baseConversion(25,8)  
print baseConversion(256,16)
print baseConversion(26,26)        