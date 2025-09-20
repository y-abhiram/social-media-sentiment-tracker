# analyze_sentiment.py
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    score = analyzer.polarity_scores(text)
    return score['compound']  # returns -1 (negative) to 1 (positive)



