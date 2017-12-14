import configparser
import tweepy

config = configparser.ConfigParser()
config.read('twitter-app-credentials.txt')
consumer_key = config['DEFAULT']['consumerKey']
consumer_secret = config['DEFAULT']['consumerSecret']
access_key = config['DEFAULT']['accessToken']
access_secret = config['DEFAULT']['accessTokenSecret']


print (consumer_key)
print (consumer_secret)
print (access_key)
print (access_secret)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth)

a = api.followers()
for x in a:
    print x

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text