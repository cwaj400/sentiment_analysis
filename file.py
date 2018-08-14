from textblob import TextBlob
import tweepy


consumer_key = ''
consumer_secret = ''

access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
    text = tweet.text
    analysis = TextBlob(text)
    print(tweet)
    print(analysis.sentiment)
