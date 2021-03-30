from datetime import date
import datetime
import tweepy
import csv

CONSUMER_KEY = 'x'
CONSUMER_SECRET = 'x'
ACCESS_KEY = 'x'
ACCESS_SECRET = 'x'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)

#the until parameter limits the collection to tweets sent just before the specified day (11:59pm the previous day)
filename = "data.csv"

with open(filename, mode = 'w') as data:
	fieldnames = ['index', 'info']
	data_writer = csv.DictWriter(data, fieldnames = fieldnames)
	for i in range(7):
		#This initializes dates such that the range is 1 day
		dUntil = datetime.datetime.now() - datetime.timedelta(days = i)
		dSince = datetime.datetime.now() - datetime.timedelta(days = i+1)
		#Change q pararmeter to fetch tweets of a different topic
		#Change items parameter to fetch x amount of tweets for each date range
		tweets = tweepy.Cursor(api.search, q="$GME", tweet_mode = "extended", since=dSince.strftime("%Y-%m-%d"), until=dUntil.strftime("%Y-%m-%d"), lang='en').items(1000)
		i = 1
		print(type(tweepy))
		for tweet in tweets:
			try:
				data_writer.writerow({'index': i, 'info': tweet.retweeted_status.full_text.encode('utf-8')})
			except AttributeError:
				data_writer.writerow({'index': i, 'info': tweet.full_text.encode('utf-8')})
			i = i + 1
