from datetime import date
from textblob import TextBlob
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime
import tweepy
import json
import csv

CONSUMER_KEY = 'X'
CONSUMER_SECRET = 'X'
ACCESS_KEY = 'X'
ACCESS_SECRET = 'X'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)

# the until parameter limits the collection to tweets sent just before the specified day (11:59pm the previous day)
filename = "data.csv"
sub_arr = [0, 0]
pol_arr = [0, 0, 0]

with open(filename, mode='w') as data:
    fieldnames = ['index', 'info']
    data_writer = csv.DictWriter(data, fieldnames=fieldnames)
    data_writer.writeheader()
    for i in range(7):
        # This initializes dates such that the range is 1 day
        dUntil = datetime.datetime.now() - datetime.timedelta(days=i)
        dSince = datetime.datetime.now() - datetime.timedelta(days=i + 1)
        # Change q pararmeter to fetch tweets of a different topic
        # Change items parameter to fetch x amount of tweets for each date range
        tweets = tweepy.Cursor(api.search, q="twitch", tweet_mode="extended", since=dSince.strftime("%Y-%m-%d"),
                               until=dUntil.strftime("%Y-%m-%d"), lang='en').items(143)
        i = 1
        # print(type(tweepy))
        for tweet in tweets:
            try:
                data_writer.writerow({'index': i, 'info': tweet.retweeted_status.full_text.encode('utf-8')})
            except AttributeError:
                data_writer.writerow({'index': i, 'info': tweet.full_text.encode('utf-8')})
            i = i + 1

# Makes a percentage out of the totals for each category
# Neural, Negative, Positive OR Objective, Subjective
def convert_to_perc(perc):
    total = 0.0
    for i in perc:
        total += i
    for i in range(len(perc)):
        perc[i] = perc[i] / total


# Makes a pie chart of polarity or subjectivity data (percentage)
def make_piechart(arr, i):
    convert_to_perc(arr)
    if i == 0:
        labels = 'Negative', 'Neutral', 'Positive'
        fig1, ax1 = plt.subplots()
        ax1.pie(arr, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.title('Sentiment Analysis - Polarity Pie Chart')
    else:
        labels = 'Objective', 'Subjective'
        fig1, ax1 = plt.subplots()
        ax1.pie(arr, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.title('Sentiment Analysis - Subjectivity Pie Chart')

    if i == 0:
        plt.savefig('pol_piechart.png')
    else:
        plt.savefig('sub_piechart.png')
    plt.clf()


# Makes a bar chart of polarity or subjectivity data (total count)
def make_barchart(arr, i):
    if i == 0:
        labels = ['Negative', 'Neutral', 'Positive']
        ypos = np.arange(len(labels))
        plt.title("Sentiment Analysis - Polarity Bar Chart")
        plt.ylabel("Count")
        plt.xticks(ypos, labels)
        plt.bar(ypos, arr, label='Count')
        plt.legend()
    else:
        labels = ['Objective', 'Subjective']
        ypos = np.arange(len(labels))
        plt.title("Sentiment Analysis - Subjectivity Bar Chart")
        plt.ylabel("Count")
        plt.xticks(ypos, labels)
        plt.bar(ypos, arr, label='Count')
        plt.legend()

    if i == 0:
        plt.savefig('pol_barchart.png')
    else:
        plt.savefig('sub_barchart.png')
    plt.clf()


# Tallies the total count
# Neutral, Negative, Positive for polarity
# Objective, Subjective for subjectivity
def get_pol_sub(value, perc, i):
    if i == 0:
        if value > 0:
            perc[2] += 1
        elif value == 0:
            perc[1] += 1
        else:
            perc[0] += 1
    else:
        if 0 <= value < 0.5:
            perc[0] += 1
        else:
            perc[1] += 1


# This is an updated implementation for the function in 'sent_ana.py'
def get_text_sub(data):
    i = TextBlob(data).sentiment.subjectivity
    get_pol_sub(i, sub_arr, 1)
    return i


# This is an updated implementation for the function in 'sent_ana.py'
def get_text_pol(data):
    i = TextBlob(data).sentiment.polarity
    get_pol_sub(i, pol_arr, 0)
    return i


df = pd.read_csv('data.csv')

df['Subjectivity'] = df['info'].apply(get_text_sub)
df['Polarity'] = df['info'].apply(get_text_pol)

print(sub_arr)
print(pol_arr)
pol_arr_count = pol_arr

make_barchart(pol_arr, 0)
make_piechart(pol_arr, 0)

make_barchart(sub_arr, 1)
make_piechart(sub_arr, 1)
