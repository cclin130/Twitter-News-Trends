file = open('tweets.txt', 'r')
sortedTweets = open('sortedTweets.txt', 'w')
wordList = [["", 0]]

#function loops through line and calls check function on each word
def checkLine(string, topic):
    temp = ""
    for x in range(0, len(string)):
        if (string[x] >= 'a' and string[x] <= 'z'):
          temp +=string[x]
        else:
            if (temp != " " and temp != "" and temp != topic and len(temp)>2):
                addWord(temp)
            temp = ""

    if (temp != " " and temp != "" and temp != topic and len(temp)>2):
        addWord(temp)

#function checks each word against existing database
def addWord(string):
    stopwords = open('stopWords.txt', 'r')
    isNewString = True
    isStopWord = False

    #filter out stop words
    for line in stopwords:
        #print(line.rstrip())
        if string == line.rstrip():
            isStopWord = True
            break

    if isStopWord == False:
        # check if string is a new entry
        for x in range(len(wordList)):
            if string == wordList[x][0]:
                wordList[x][1] = wordList[x][1] + 1
                #print(wordList[x][0] + " " + str(wordList[x][1]))
                isNewString = False
        if isNewString == True:
            wordList.append([string, 1])
            #print(wordList[int(len(wordList)-1)][0] + " " + str(wordList[int(len(wordList)-1)][1]))

#def filter (topic):
topic = "memo"

for line in file:
    checkLine(line.lower(), topic)

sorted = sorted(wordList, key=lambda l:l[1], reverse=True)

for x in range(10):
   print(sorted[x][0] + " " + str(sorted[x][1]))

for x in range(10):
    toWrite = sorted[x][0] + " " + str(sorted[x][1] + "\n")
    sortedTweets.write(toWrite)