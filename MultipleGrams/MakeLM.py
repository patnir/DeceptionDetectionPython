def processFile(fName, grams):
    import csv
    f = open(fName)
    data = list(csv.reader(f, delimiter=','))
    out = []
    k = 0
    for row in data:
        row = row[0].split("|")
        if len(row) != 2: continue
        s = str(row[0]).lower().split("[a-zA-Z]+")
        s = s[0].split(" ")
        for i in range(0, len(s) - grams):
            temp = s[i]
            for j in range(i + 1, i + grams):
                temp += ' ' + s[j]
            out.append(temp)
    del data
    return out

def getIndeces(d):
    indexes = []
    for key in d:
        if key[1] == ' ': key = key[0] + '_'
        index = key[:2]
        if index not in indexes: indexes.append(index)
    # print(indexes)
    return indexes

def getDictFromGoogle(fName, ngrams, getGoogle, indicFile):
    grams = processFile(fName, ngrams)
    gDict = dict()
    for row in grams:
        gDict[row] = 1
    del grams
    # ind = getIndeces(gDict)
    ind = readIndices(indicFile)

    if getGoogle is False: return gDict
    from google_ngram_downloader import readline_google_store
    for iterator in range(0, len(ind)):
        row = ind[iterator]
        d = [row]
        try:
            fName, url, records = next(readline_google_store(ngram_len=ngrams, indices=d))
        except Exception:
            print("Cannot find : " + row)
            continue
        s = len(gDict)
        count = -1
        mc = 0
        found = 0
        import time
        tim = time.time()
        while True:
            if s <= 0: break
            try:
                record = next(records)
                w = record.ngram.lower()
                temp = w
                if count == -1: print("Started")
                count += 1
                if count == 1000000:
                    ntim = time.time()
                    count = 0
                    mc += 1
                    print("CheckPoint: " + w + " timeTakenForMil: " + str(ntim - tim) + " Mil Count = " + str(
                        mc) + " Found = " + str(found))
                    tim = ntim
                if (str(temp.split("[a-zA-Z]+")) != w):
                    continue
                if w in gDict:
                    if gDict[w] == 1:
                        found += 1
                        print("Found: " + w)
                    gDict[w] += record.match_count
            except StopIteration:
                writeToGramData(gDict, ngrams, row + '.txt')
                break
    return gDict

def readIndices(fName):
    import csv
    f = open(fName)
    data = list(csv.reader(f, delimiter=','))
    return data

def writeToGramData(d, grams, outputFname):
    all = []
    for key in d:
        t = []
        t.append(key)
        t.append(d[key])
        all.append(t)
    print(all)
    import csv
    with open(str(grams) + outputFname, 'w', newline="") as fp:
        a = csv.writer(fp, delimiter=',')
        a.writerows(all)

def printIndices(gramDict):
    import csv
    with open('indices.txt', 'w', newline="") as fp:
        a = csv.writer(fp, delimiter=',')
        l = getIndeces(gramDict)
        for i in range(0, len(l)):
            t = []
            t.append(l[i][0] + "" + l[i][1])
            l[i] = t
        a.writerows(l)

numGrams = 3
gramDict = getDictFromGoogle('data.txt', numGrams, True, '1.txt')       #Change the input file name for each process(1.txt to 2.txt)
writeToGramData(gramDict, numGrams, 'output-1.csv')                    #Change the process output file name