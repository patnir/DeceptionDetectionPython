# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 11:29:54 2016

@author: Rahul Patni
"""

# loading all features


def loadData():
    lies = "SmallLies.csv"
    truth = "SmallTruths.csv"
    lptr = open(lies)
    for i in lptr:
        print i
    
    
def main():
    loadData()
    
main()