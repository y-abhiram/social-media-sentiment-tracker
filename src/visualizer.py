# visualizer.py

import seaborn as sns
import matplotlib.pyplot as plt

def plot_sentiment_trends(df):
    trend = df.groupby(['date', 'sentiment']).size().unstack().fillna(0)
    trend.plot(kind='line', figsize=(10, 5))
    plt.title("Sentiment Trends Over Time")
    plt.xlabel("Date")
    plt.ylabel("Tweet Count")
    plt.show()

