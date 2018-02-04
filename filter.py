file = open('tweets.txt', 'r')
stopwords = open('stopWords.txt', 'r')
newfile = open('wordCounts.txt', 'w')
wordList = [["", 0]]

#function loops through line and calls check function on each word
def checkLine(string):
    #print(string)
    temp = ""
    for x in range(0, len(string)):
        if (string[x] >= 'a' and string[x] <= 'z'):
          temp +=string[x]
        else:
            if (temp != " "):
                checkWord(temp)
            temp = ""

    if (temp != " "):
        checkWord(temp)

#function checks each word against existing database
def checkWord(string):
    isNewString = True
    isStopWord = False

    #filter out stop words
    for line in stopwords:
        if string == line:
            isStopWord == True
            #print(string)

    if isStopWord == False:
        # check if string is a new entry
        for x in range(len(wordList)):
            if string == wordList[x][0]:
                wordList[x][1] = wordList[x][1] + 1
                #print(wordList[x][0] + " " + str(wordList[x][1]))
                isNewString = False
        if isNewString == True:
            wordList.append([string, 1])
            print(wordList[int(len(wordList)-1)][0] + " " + str(wordList[int(len(wordList)-1)][1]))

#----------------main---------------
for line in file:
    checkLine(line.lower())