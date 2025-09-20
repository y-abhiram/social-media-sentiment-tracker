# twitter_scraper.py

import tweepy
import pandas as pd
from config import twitter_config

def get_twitter_client():
    auth = tweepy.OAuthHandler(twitter_config.API_KEY, twitter_config.API_SECRET)
    auth.set_access_token(twitter_config.ACCESS_TOKEN, twitter_config.ACCESS_SECRET)
    return tweepy.API(auth, wait_on_rate_limit=True)

def fetch_tweets(query, count=100):
    client = get_twitter_client()
    tweets = tweepy.Cursor(client.search_tweets, q=query, lang='en', tweet_mode='extended').items(count)
    
    data = [[tweet.created_at, tweet.user.screen_name, tweet.full_text] for tweet in tweets]
    return pd.DataFrame(data, columns=["timestamp", "user", "text"])

