# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 23:11:25 2015
An abstract data type for Fraction 
This data type supports addition,subtraction,division, multiplication,
print and comparison operations.
@author: caped_crusader
"""

class Fraction:
    #provide constructor to create the data object
    def __init__(self,top,bottom):
        self.num = top
        self.denom = bottom
        
     # add a show method to print the object   
    def show(self):
        print '%d/%d' %(self.num,self.denom)
        
     # modify the __str__ method to print the fraction   
    def __str__(self):
        return "%d/%d" %(self.num,self.denom)
        
    # modifying the __add__ function
    def __add__(self,otherfunction):
        # dude, get the numerator 
        newNum = self.num*otherfunction.denom + self.denom*otherfunction.num
        newDenom = self.denom + otherfunction.denom
        common = self.gcd(newNum,newDenom)
        return Fraction(newNum//common,newDenom//common)        
   
    def gcd(self,m,n):
        if m%n == 0:
            return n
        else: 
            return gcd(n,m%n)
    
    def __eq__(self,f2):
        num1 = self.num*f2.denom
        num2 = f2.num*self.denom
        if num1 == num2:
            return True
        else:
            return False
            
    def __multiply__(self,other):
        num1 = self.num*other.num
        denom1 = self.denom * other.denom
        return Fraction(num1,denom1)
        
    def __division__(self,other):
        return Fraction(self.num*other.denom,self.denom*other.num)
        
    def __subtract__(self,other):
        num1 = self.num*other.denom - other.num*self.denom
        num2 = self.denom*other.denom
        return Fraction(num1,num2)
        
    def __greaterThan__(self,other):
        num1 =self.num*other.denom - other.num*self.denom
        if num1 > 0:
            return True
        elif num1 == 0:
            return 'Equal'
        else:
            return False
        
myf = Fraction(3,4)
myf.show() # envoking show method for printing

# envoking __str__ to print the fraction
str(myf)
myf.__str__()
print myf

# using the addition method fro fraction
f1 = Fraction(1,2)
f2 = Fraction(1,2)

print f1.__add__(f2)
print f1 + f2

print f1 == f2
print f1.__eq__(f2)

#print f1*f2
print f1.__multiply__(f2)
f1 = Fraction(11,4)
f2 = Fraction(3,7)

print f1.__multiply__(f2)
print f1.__division__(f2)
print f1.__subtract__(f2)
print f1.__greaterThan__(f2)

























