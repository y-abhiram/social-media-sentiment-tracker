from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__)

def load_data():
    df = pd.read_csv('tweets_sentiment.csv')
    df['created_at'] = pd.to_datetime(df['created_at'])
    return df

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/data')
def get_data():
    df = load_data()
    return jsonify(df.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)



'''
from flask import Flask, render_template
import pandas as pd
import plotly.express as px
import plotly
import json
from datetime import datetime

app = Flask(__name__)

def load_data():
    df = pd.read_csv('/home/abhiram1289/Desktop/social-media-sentiment-tracker/tweets_sentiment.csv')
    df['created_at'] = pd.to_datetime(df['created_at'])

    # Label sentiment
    df['sentiment_label'] = df['sentiment'].apply(
        lambda x: 'positive' if x > 0.1 else ('negative' if x < -0.1 else 'neutral')
    )

    return df

@app.route('/')
def index():
    df = load_data()

    # Summary stats
    total_tweets = len(df)
    avg_sentiment = df['sentiment'].mean()
    sentiment_counts = df['sentiment_label'].value_counts().to_dict()
    positive = sentiment_counts.get('positive', 0)
    neutral = sentiment_counts.get('neutral', 0)
    negative = sentiment_counts.get('negative', 0)

    # Scatter Plot
    scatter_fig = px.scatter(
        df, x='created_at', y='sentiment', color='sentiment_label',
        title='Sentiment Over Time',
        hover_data=['text'],
        color_discrete_map={'positive': 'green', 'neutral': 'blue', 'negative': 'red'}
    )
    scatter_fig.update_layout(hovermode="closest")
    scatter_plot_json = json.dumps(scatter_fig, cls=plotly.utils.PlotlyJSONEncoder)

    # Pie Chart
    pie_df = df['sentiment_label'].value_counts().reset_index()
    pie_df.columns = ['sentiment', 'count']
    pie_fig = px.pie(pie_df, names='sentiment', values='count', title='Sentiment Distribution')
    pie_plot_json = json.dumps(pie_fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('dashboard.html',
                           scatter_plot_json=scatter_plot_json,
                           pie_plot_json=pie_plot_json,
                           total=total_tweets,
                           avg=round(avg_sentiment, 3),
                           positive=positive,
                           neutral=neutral,
                           negative=negative
                           )

if __name__ == '__main__':
    app.run(debug=True)


'''
