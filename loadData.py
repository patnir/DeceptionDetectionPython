# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 11:29:54 2016

@author: Rahul Patni
"""

# loading all features


def loadData():
    lies = "100OnlyLies.csv"
    truth = "100OnlyTruths.csv"
    lptr = open(lies)
    for i in lptr:
        i = i.rstrip()
        print i
    
    
def main():
    loadData()
    
main()