########### Python 3.2 #############
def getFromMicrosoftLM(words, n):
    import http.client, urllib.request, urllib.parse, urllib.error, base64

    headers = {
        # Request headers
        'Ocp-Apim-Subscription-Key': code,
    }

    params = urllib.parse.urlencode({
        # Request parameters
        'model': 'body',
        'text': words,
        'order': str(n),
        'maxNumOfCandidatesReturned': '1'
    })

    try:
        conn = http.client.HTTPSConnection('api.projectoxford.ai')
        conn.request("POST", "/text/weblm/v1.0/breakIntoWords?%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        import json
        d = str(data)
        j = json.loads(d[2:-1])
        retVal = j['candidates'][0]['probability']
        conn.close()
    except Exception as e:
        print("Some Error")
        retVal = 0
    return retVal

    ####################################


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


def writeToGramData(d, grams, outputFname):
    all = []
    for key in d:
        t = []
        t.append(key)
        t.append(d[key])
        all.append(t)
    #print(all)
    import csv
    with open(str(grams) + outputFname, 'w', newline="") as fp:
        a = csv.writer(fp, delimiter=',')
        a.writerows(all)


def createGramDict(data, n):
    gDict = dict()
    counter = 0
    p = 10
    import time
    tim = time.time()
    for row in data:
        if row in gDict: continue
        if counter >= 900:
            p+=1
            print("900 Checkpoint: " + str(p-9))
            import time
            writeToGramData(gDict, n, "intermediateMicrosoftLM.csv")

            sleepTime = 60 - time.time() + tim
            if sleepTime > 0: time.sleep(sleepTime)
            tim = time.time()

            counter = 0
        val = getFromMicrosoftLM(row, n)
        counter+=1
        if val == 0: continue
        gDict[row] = val
    writeToGramData(gDict, n, "MicrosoftLM.csv")


code = 'f78266c07c844fc2b698595c99150c78'                       #Change this to your code
n = 5                                                     #Change this to whatever n gram you want
data = processFile('data.txt', n)
print("No of queries: " + str(len(data)))
createGramDict(data, n)
