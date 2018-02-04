import tweepy
import sys

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

consumer_key = 'rxQyLQiaXDO5yEXNgvoFhnHK0'
consumer_secret = 'YFRWjTqut9pKsQYrgCUb7DhpZmnRV6B81dsM2phGuojpQlDRAo'
access_token = '3288616639-w1YkmHiMe0CeCi2gT7W6L6IUMuuelEd459vpTAe'
access_token_secret = '4odnb7CA4IjXcXTeXhl7js7ig6Gw6DK5jDtSIaRZVsJOr'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def extract():
    topic = input("Enter a hashtag: #")
    count = input("Enter number of tweets: ")

    if (topic[0] != "#"):
        hashtag = "#" + str(topic)

    file = open("extracted.txt", "w")
    c = 0

    for tweet in tweepy.Cursor(api.search, hashtag, count = 100, lang="en", since_id=2017).items(): #get tweets containing the input hashtag

        s = str(str(tweet.text).translate(non_bmp_map).encode("utf-8"))
        print(s) #print tweets
        file.write(s)
        c = c + 1

        if (c == int(count)): # display the most recent results, up to user specified amount
            break

    return topic, "extracted.txt"