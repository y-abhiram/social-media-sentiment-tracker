'''
# main.py
from fetch_tweets import fetch_tweets
from analyze_sentiment import analyze_sentiment
from store_data import store_to_csv
from visualize import plot_sentiment_over_time

def run_pipeline(query):
    tweets = fetch_tweets(query)
    for tweet in tweets:
        tweet['sentiment'] = analyze_sentiment(tweet['text'])
    store_to_csv(tweets)
    plot_sentiment_over_time()

if __name__ == "__main__":
    run_pipeline("OpenAI")
'''
# main.py

from fetch_tweets import fetch_tweets
from analyze_sentiment import analyze_sentiment
from store_data import store_to_csv

def run(query):
    tweets = fetch_tweets(query)
    for tweet in tweets:
        tweet['sentiment'] = analyze_sentiment(tweet['text'])
        print(f"{tweet['created_at']} | {tweet['sentiment']:.2f} | {tweet['text'][:80]}")

    store_to_csv(tweets)
    print(f"✅ {len(tweets)} tweets processed and stored in tweets_sentiment.csv")

if __name__ == "__main__":
    run("OpenAI")  # 🔁 You can change this to any topic/brand

