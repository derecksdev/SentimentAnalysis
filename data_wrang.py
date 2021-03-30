from textblob import TextBlob
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv

def convert_to_perc(perc):
    total = 0.0
    for i in perc:
        total += i
    for i in range(len(perc)):
        perc[i] = perc[i] / total


def make_piechart(arr):
    convert_to_perc(arr)

    labels = 'Negative', 'Neutral', 'Positive'
    fig1, ax1 = plt.subplots()
    ax1.pie(arr, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.savefig('pie_char.png')


def get_pol_sub(value, perc):
    if value > 0:
        perc[2] += 1
    elif value == 0:
        perc[1] += 1
    else:
        perc[0] += 1

# This is an updated implementation for the function in 'sent_ana.py'
def get_text_sub(data):
    i = TextBlob(data).sentiment.subjectivity
    get_pol_sub(i, sub_arr)
    return i

# This is an updated implementation for the function in 'sent_ana.py'
def get_text_pol(data):
    i = TextBlob(data).sentiment.polarity
    get_pol_sub(i, pol_arr)
    return i

# This will get the amount of times a word has been used
# Just need to find a way to pick a word that you want to check for 
#def freq_of_words(data, word_to_check):
 
 #   i = TextBlob(data)
  #  i.word_counts[word_to_check]
   # return i