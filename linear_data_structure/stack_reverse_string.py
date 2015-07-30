# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 00:16:24 2015

@author: caped_crusader
"""

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
        
    def show(self):
        print self.items
        
# implementation of method 1
        
def revstring(mystr):
    for i in range(len(mystr)):
        out_str.push(mystr[i])
   
    ans = ''
    for i in range(out_str.size()):
        ans = ans+out_str.peek()
        out_str.pop()
    return ans

    
 # implementation of method 2       
in_str = Stack()
out_str = Stack()

def reverse(str):
    for i in str:
        in_str.push(i)
    in_str.show()
    
    length = len(str)
    i = 0
    while i < length:
        out_str.push(in_str.pop())
        i = i + 1
    out_str.show()
      
reverse('tihom')


# implementation by a simple list

def Reverse(str):
    rev = []
    for i in range(len(str)-1,-1,-1):
        rev.append(str[i])
    
    print 'original string --> ', str
    print 'reversed string --> ', "".join(rev)
    
Reverse('tihom')
    

 
    
    

