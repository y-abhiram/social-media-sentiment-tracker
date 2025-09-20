# dashboard.py

import streamlit as st
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

st.title("Twitter Sentiment Dashboard")

df = pd.read_csv('data/cleaned_tweets.csv')
st.line_chart(df.groupby('date')['sentiment'].value_counts().unstack().fillna(0))

if st.checkbox("Show WordCloud for Positive Tweets"):
    text = ' '.join(df[df['sentiment'] == 'positive']['text'])
    wc = WordCloud(width=800, height=400).generate(text)
    st.image(wc.to_array())

