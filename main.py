import tweets
import filter
import bar

#extract tweets into 'extracted.txt'
topic, fileName = tweets.extract()
#filter topics and sort, send to 'sortedTweets.txt'
filter.filter(topic, fileName)
#convert sortedTweets.txt into a bar chart
bar.toBarChart(topic)
