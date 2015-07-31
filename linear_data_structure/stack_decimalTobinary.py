# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 13:11:34 2015

@author: caped_crusader
"""

class Stack:
    def __init__(self):
        self.items = []
        
    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return self.items == []
        
    def push(self,item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
        
    def peek(self):
        return self.items[len(self.items)-1]
    
    def show(self):
        print self.items
        

def divideBy2(num):
    s = Stack()
    while num >= 1:
        s.push(num%2)
        num = num//2
    binary = ''
    while not s.isEmpty():
        binary = binary + str(s.pop())
        
    return binary
    
print divideBy2(233)
print divideBy2(42)