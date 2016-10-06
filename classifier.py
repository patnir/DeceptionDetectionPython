# -*- coding: utf-8 -*-
"""
Created on Mon Oct 03 23:38:25 2016

@author: Rahul Patni
"""

# classifier

from sklearn import svm

import numpy as np

def loadFeaturesFromFile(filename):
    fptr = open(filename)
    features = []
    for i in fptr:
        features.append(i.rstrip())
    return features        
        

def loadTestingAndTrainingData(positive, negative):
    fptr = open(positive)
    dataSet = []
    labels = []
    for i in fptr:
        dataSet.append(i.rstrip())
        labels.append(1)
    fptr = open(negative)
    for i in fptr:
        dataSet.append(i.rstrip())
        labels.append(0)
        
    return dataSet, labels

def crossValidation(dataSet, labels):
    Training = [[], [], [], [], []]
    Testing = [[], [], [], [], []]
        
    for i in range(len(dataSet)):
        if i % 5 == 0:
            Testing[0].append([dataSet[i], labels[i]])
            Training[1].append([dataSet[i], labels[i]])
            Training[2].append([dataSet[i], labels[i]])
            Training[3].append([dataSet[i], labels[i]])
            Training[4].append([dataSet[i], labels[i]])
        elif i % 5 == 1:
            Testing[1].append([dataSet[i], labels[i]])
            Training[0].append([dataSet[i], labels[i]])
            Training[2].append([dataSet[i], labels[i]])
            Training[3].append([dataSet[i], labels[i]])
            Training[4].append([dataSet[i], labels[i]])
        elif i % 5 == 2:
            Testing[2].append([dataSet[i], labels[i]])
            Training[0].append([dataSet[i], labels[i]])
            Training[1].append([dataSet[i], labels[i]])
            Training[3].append([dataSet[i], labels[i]])
            Training[4].append([dataSet[i], labels[i]])
        elif i % 5 == 3:
            Testing[3].append([dataSet[i], labels[i]])
            Training[0].append([dataSet[i], labels[i]])
            Training[1].append([dataSet[i], labels[i]])
            Training[2].append([dataSet[i], labels[i]])
            Training[4].append([dataSet[i], labels[i]])
        elif i % 5 == 4:
            Testing[4].append([dataSet[i], labels[i]])
            Training[0].append([dataSet[i], labels[i]])
            Training[1].append([dataSet[i], labels[i]])
            Training[2].append([dataSet[i], labels[i]])
            Training[3].append([dataSet[i], labels[i]])
    return Training, Testing


def binarySearch(a, target):
    start = 0
    end = len(a) - 1
    while start <= end:
        mid = (start + end) / 2
        if a[mid] == target:
            return mid
        if a[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1

def settingWeights(features, Training):
    X = [0] * len(Training)
    y = [0] * len(Training)

    for i in range(len(Training)):
        presence = [0] * len(features)
        words = Training[i][0].split(" ")
        for j in words:
            index = binarySearch(features, j)
            if index != -1:
                presence[index] = 1
        X[i] = presence
        y[i] = Training[i][1]
    clf = svm.SVC()
    clf.fit(X, y)
    
    return clf
    
def checkingAccuracy(features, Testing, clf):
    total = 0
    for i in range(len(Testing)):
        words = Testing[i][0].split(" ")
        presence = [0] * len(features)
        for j in words:
            index = binarySearch(features, j)
            if index != -1:
                presence[index] = 1
        presence = np.array(presence).reshape((1, -1))
        if clf.predict(presence) == [Testing[i][1]]:
            total += 1
    return float(total) / len(Testing) * 100

def classifier(features, Training, Testing, dataSet, labels):
    total = 0
    for i in range(len(Training)):
        clf = settingWeights(features, Training[i])
        accuracy = checkingAccuracy(features, Testing[i], clf)
        print str(i + 1) + ":", str(accuracy)
        total += accuracy
    print float(total) / 5
    return
        
def main():
    features = loadFeaturesFromFile("featuresNew.txt")
    dataSet, labels = loadTestingAndTrainingData("100Truths.csv", "100Lies.csv")
    Training, Testing = crossValidation(dataSet, labels)
    classifier(features, Training, Testing, dataSet, labels)
    
    
    
        
    
main()