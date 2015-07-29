# -*- coding: utf-8 -*-
"""
Created on Tue Jul 07 16:21:36 2015

@author: caped_crusader
"""

class queue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items ==[]
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def getitem(self,index):
        return self.items[index]
        
q = queue()
q.enqueue(1)
q.enqueue(2)
print q.size()
print q.getitem(0)        



def hot_potato(names,num):
    myqueue = queue()
    for name in names:
        myqueue.enqueue(name)
    while myqueue.size() > 1:
        for i in range(num):
            myqueue.enqueue(myqueue.dequeue())
        myqueue.dequeue()
    return myqueue.getitem(0)
    
names = ["dalla","kutta","jain","namit","bohra"]
print hot_potato(names,2)
print(hot_potato(["Bill","David","Susan","Jane","Kent","Brad"],7))