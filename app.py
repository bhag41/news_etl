import pandas as pd
import sqlite3
import logging
from newsapi import NewsApiClient

logging.basicConfig(level=logging.INFO)

news_api_key = "10e55a1639ed4d509b1f3f0dbf1b62e4"
newsapi = NewsApiClient(api_key=news_api_key)

def extract_news_date():
    try:
        top_headlines = newsapi.get_top_headlines(language='en')
        logging.info(f"Top headlines response: {top_headlines}")
        articles = top_headlines.get('articles', [])
        logging.info(f"Extracted {len(articles)} articles")
        news = []
        for article in articles:
            news.append([article['title'], article['description'], article['url']])
        return news
    except Exception as e:
        logging.error(f"Error in extracting news: {e}")
        return None

articles = extract_news_date()

if articles:
    print(articles[:5])
else:
    print("No articles found")