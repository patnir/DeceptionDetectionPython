
def loadWordsAndOccurances():
    words = dict()
    filename = "JustLiesAndTruths.csv"
    fptr = open(filename)

    for i in fptr:
        j = i.rstrip().split(" ")
        for l in j:
            if l in words:
                words[l] += 1
            else:
                words[l] = 1
    print len(words)
    val = words.values()
    key = words.keys()

    wordsList = []
    
    for i in range(len(val)):
        if val[i] > 2:
            wordsList.append(key[i])
    
    print len(wordsList)
        
    fptr.close()
    return wordsList

def writeWords(words):
    filename = "featuresNew.txt"
    fptr = open(filename, 'w')
    
    words.sort()    
    
    for i in words:
        print i
        fptr.write(i + "\n")

    fptr.close()        

def main():
    words = loadWordsAndOccurances()
    print words
    writeWords(words)
    return
    
main()