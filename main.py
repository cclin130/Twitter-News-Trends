import tweets
import filter

#extract tweets into 'extracted.txt'
topic, fileName = tweets.extract()
#filter topics and sort, send to 'sortedTweets.txt'
filter.filter(topic, fileName)