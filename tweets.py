import tweepy
import sys

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

consumer_key = 'Nri3o9wMEtl5OX4etF6qiM0L4'
consumer_secret = 'CT1pYMyflbCXZeb1sYndjfPvAOfbxU5lMyzuotCI1Fv6OlmsyT'
access_token = '589929389-oWcvpIqVue8crszfC52PzJh6R8ttug6doEARnWPV'
access_token_secret = 'Ja99sCF7X1PUe7KK5BiNM9tZyGOpi5p68FrHLmGc6t57x'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

topic  = input("Enter a hashtag: #")

if (topic[0] != "#"):
    topic = "#" + str(topic)

file = open("tweets.txt", "w")
c = 0

for tweet in tweepy.Cursor(api.search, topic, count = 100, lang="en", since_id=2017).items(): #get tweets containing the input hashtag

    s = str(str(tweet.text).translate(non_bmp_map).encode('utf-8'))
    print(s) #print tweets
    file.write(s)
    c = c + 1
    if (c == 500): # display the first 500 results
        break
