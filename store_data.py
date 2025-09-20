import csv
import os

def store_to_csv(data, filename='tweets_sentiment.csv'):
    file_exists = os.path.isfile(filename)
    with open(filename, mode='a' if file_exists else 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["text", "created_at", "sentiment"])
        if not file_exists:
            writer.writeheader()
        for row in data:
            writer.writerow(row)















'''
# store_data.py

import csv

def store_to_csv(data, filename='tweets_sentiment.csv'):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["text", "created_at", "sentiment"])
        writer.writeheader()
        for row in data:
            writer.writerow(row)

# Dummy test
if __name__ == "__main__":
    sample_data = [
        {"text": "I love AI", "created_at": "2025-07-12 10:00:00", "sentiment": 0.9},
        {"text": "AI is scary", "created_at": "2025-07-12 11:00:00", "sentiment": -0.6}
    ]
    store_to_csv(sample_data)
    print("Sample data written to tweets_sentiment.csv ✅")
'''
