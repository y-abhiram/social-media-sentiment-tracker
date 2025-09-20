# visualize.py
import pandas as pd
import matplotlib.pyplot as plt

def plot_sentiment_over_time(csv_file='tweets_sentiment.csv'):
    df = pd.read_csv(csv_file, parse_dates=['created_at'])
    df['created_at'] = pd.to_datetime(df['created_at'])
    df.set_index('created_at', inplace=True)
    df = df.resample('H').mean()  # average sentiment per hour
    df['sentiment'].plot(title='Sentiment Over Time')
    plt.xlabel('Time')
    plt.ylabel('Sentiment')
    plt.show()

