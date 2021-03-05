from datetime import date
import datetime
import tweepy

CONSUMER_KEY = 'x'
CONSUMER_SECRET = 'x'
ACCESS_KEY = 'x'
ACCESS_SECRET = 'x'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)

#the until parameter limits the collection to tweets sent just before the specified day (11:59pm the previous day)

for i in range(7):
	#This initializes dates such that the range is 1 day
	dUntil = datetime.datetime.now() - datetime.timedelta(days = i)
	print("dUntil: " + dUntil.strftime("%Y-%m-%d"))
	dSince = datetime.datetime.now() - datetime.timedelta(days = i+1)
	print("dSince: " + dSince.strftime("%Y-%m-%d"))
	#Change q pararmeter to fetch tweets of a different topic
	#Change items parameter to fetch x amount of tweets for each date range
	tweets = tweepy.Cursor(api.search, q="$GME", tweet_mode = "extended", since=dSince.strftime("%Y-%m-%d"), until=dUntil.strftime("%Y-%m-%d"), lang='en').items(2)
	i = 1
	print(type(tweepy))
	for tweet in tweets:
		try:
			print(str(i) + ": " + tweet.retweeted_status.full_text)
		except AttributeError:
			print(str(i) + ": " + tweet.full_text)
		i = i + 1
