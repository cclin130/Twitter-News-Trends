import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

def toBarChart(topic):
    tweetsdata = open("sortedTweets.txt","r") # open the file
    words = tweetsdata.readline().split(" ") # reads the first line and puts it in a list
    words.pop() # last element of the list is '\n'. Remove it

    number = tweetsdata.readline().split(" ") # reads the second line. Put in list
    number.pop() # Remove last element
    number = list(map(int, number)) # convert the string list to int list

    y_pos = np.arange(len(number))
    plt.bar(y_pos, number, align = 'center')
    plt.xticks(y_pos, words)
    plt.ylabel('No. of times each word appeared in different tweets')
    plt.title('Top 10 words associated with #' + topic)

    plt.show()
