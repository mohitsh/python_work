# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 23:01:00 2015

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
        
        
def InfixToPostfix(str):
    prec = {"*":3, "/":3, "+":2, "-":2, "(":1}
    opStack = Stack()
    outputList = []
    inputList = str.split()
    check1 = 'ABCDEFGHIJKLMNOPQURSTUVWXYZ'
    check2 = '1234567890'
    for i in inputList:
        if i in check1 or i in check2:
            outputList.append(i)
        elif i == "(":
            opStack.push(i)
        elif i == ")":
            toptoken = opStack.pop()
            while toptoken != "(":
                outputList.append(toptoken)
                toptoken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[i]):
                outputList.append(opStack.pop())
            opStack.push(i)
    
    while not opStack.isEmpty():
        outputList.append(opStack.pop())
    return "".join(outputList)
    
    

print InfixToPostfix("A * B + C * D")
print InfixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )")
    