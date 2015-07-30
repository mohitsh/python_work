# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 22:21:46 2015

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

