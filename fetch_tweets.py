# fetch_tweets.py

import tweepy
from twitter_config import BEARER_TOKEN

def fetch_tweets(query, max_results=100):
    client = tweepy.Client(bearer_token=BEARER_TOKEN)
    
    response = client.search_recent_tweets(
        query=query,
        max_results=min(max_results, 100),
        tweet_fields=['created_at', 'lang'],
    )

    tweets = []
    for tweet in response.data or []:
        if tweet.lang == 'en':
            tweets.append({
                'text': tweet.text,
                'created_at': tweet.created_at.strftime("%Y-%m-%d %H:%M:%S")
            })

    return tweets

