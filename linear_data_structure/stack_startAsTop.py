# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 00:03:27 2015

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
        self.items.insert(0,item)
        
    def pop(self):
        return self.items.pop(0)
        
    def peek(self):
        return self.items[0]
        
        
s = Stack()
print 'is empty --> ', s.isEmpty()
print 'size --> ', s.size()
s.push('dalakoti')
print 'is empty --> ', s.isEmpty()
print 'size --> ', s.size()
print s.peek()
s.push('aditya')
print 'is empty --> ', s.isEmpty()
print 'size --> ', s.size()
print s.peek()
s.push('bohra')
print 'is empty --> ', s.isEmpty()
print 'size --> ', s.size()
print s.peek()
print s.pop()
print 'size --> ', s.size()
print s.pop()
print 'size --> ', s.size()
