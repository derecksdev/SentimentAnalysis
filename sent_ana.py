from textblob import TextBlob
import pandas as pd
import numpy as np 
import csv

def get_text_sub(data):
    return TextBlob(data).sentiment.subjectivity

def get_text_pol(data):
    return TextBlob(data).sentiment.polarity

df = pd.read_csv('data.csv')

df['Subjectivity'] = df['Tweet'].apply(get_text_sub)
df['Polarity'] = df['Tweet'].apply(get_text_pol)

print(df)
