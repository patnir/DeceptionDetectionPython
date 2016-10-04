# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 11:29:54 2016

@author: Rahul Patni
"""

# loading all features


def loadData():
    files = ["100LiesAndLabels.csv", "100TruthsAndLabels.csv"]
    words = set()
    for x in files:
        lines = open(x)
        for i in lines:
            i = i.rstrip()
            i = i.split('.\',')
            j = i[0].split(' ')
            for k in j:
                words.add(k)
    words = list(words)
    words.sort()
    print words
        
    
    
def main():
    loadData()
    
main()