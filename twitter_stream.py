# twitter_stream.py
import tweepy
from sentiment import analyze_sentiment  # Your existing function
from store_data import store_to_csv     # Your existing CSV storage
import datetime

# Set your credentials
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAKsO3AEAAAAARqlDQhDHZXZcO5JH5PPHAMyynvo%3DF0WqJtcWIl3j3BPoKP0PC2jSnvEJjkmlLXqG6AIOMR9tr31sXc'

class TweetStream(tweepy.StreamingClient):
    def __init__(self, bearer_token):
        super().__init__(bearer_token)
        self.data = []

    def on_tweet(self, tweet):
        text = tweet.text
        sentiment = analyze_sentiment(text)
        created_at = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

        tweet_data = {"text": text, "created_at": created_at, "sentiment": sentiment}
        self.data.append(tweet_data)

        print(tweet_data)

        # Optional: Save every 10 tweets
        if len(self.data) >= 10:
            store_to_csv(self.data)
            self.data = []

# Start streaming
if __name__ == "__main__":
    stream = TweetStream(BEARER_TOKEN)
    stream.add_rules(tweepy.StreamRule("AI OR Artificial Intelligence"))
    stream.filter(tweet_fields=["created_at"])

