# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 22:32:03 2015

@author: caped_crusader
"""

import random 
alpha = 'abcdefghijklmnopqurstuvwxyz '
goal = "methinks it is like a weasel"

def generate():
    sentence =  ''
    for i in range(1,29):
        randomInt = random.randint(1,27)
        sentence = sentence + alpha[randomInt]
    return sentence


def score(line):
    genLine = line
    #print genLine
    #print len(genLine)
    #print goal
    #print len(goal)
    scoreRec = 0
    for i in range(1,28):
        if genLine[i] == goal[i]:
            scoreRec = scoreRec + 1
    #return genLine        
    return scoreRec
    

def calling():
    line_arr=[]
    score_record_arr = []
    for i in range(1,1001):
        line = generate()
        line_arr.append(line)
        score_record = score(line)
        score_record_arr.append(score_record)
        #print line
        #print score_record
        
    maxscore = max(score_record_arr)
    #print maxscore
    maxindex = score_record_arr.index(maxscore)
    maxline = line_arr[maxindex]
    print maxline
    print maxscore
    
        
    
    
    






