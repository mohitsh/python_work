# -*- coding: utf-8 -*-
"""
Created on Thu Jul 02 20:19:35 2015

@author: caped_crusader
"""


def generator():
    #import string
    lowerc = "mohit"
    #lowerc = lowerc + " "
    word = []
    for i in range(len(lowerc)):
        from random import randint
        randnum = randint(0,4)
        letter = lowerc[randnum]
        word.append(letter)
    
    return ''.join(word)

def compare():
    target = "mohit"
    ans = generator()
    score = 0
    for i in range(len(ans)):
        if target[i] == ans[i]:
            score = score + float(1)/27*100 
        else:
            pass
    print ans, score
    #print score
    
    
def ask():
    for i in range(100):
        compare()s
        