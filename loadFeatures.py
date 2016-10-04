
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
        if val[i] > 4 and val[i] < 20:
            wordsList.append(key[i])
    
    print len(wordsList)
        
    return wordsList

def main():
    words = loadWordsAndOccurances()
    print words
    return
    
main()