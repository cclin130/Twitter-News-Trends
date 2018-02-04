file = open('tweets.txt', 'r')
stopwords = open('stopWords.txt', 'r')


#function loops through line and calls check function on each word
def addToList(string):
    print(string)
    temp = ""
    for x in range(0, len(string)):
        if (string[x] >= 'a' and string[x] <= 'z'):
          temp +=string[x]
        else:
            #print(temp)
            check(temp)
            temp = ""
    #print(temp)
    check(temp)

#function checks each word against existing database
def check(string):
    isNewString = False
    isStopWord = False
    wordList = [["", ""]]

    #filter out stop words
    for line in stopwords:
        if string == line:
            isStopWord == True

    if isStopWord == False:
        # check if string is a new entry
        for x in range(len(wordList)):
            


#----------------main---------------
for line in file:
    addToList(line.lower())