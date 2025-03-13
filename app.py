import pandas as pd
import sqlite3
import logging
from newsapi import NewsApiClient

news_api_key = "10e55a1639ed4d509b1f3f0dbf1b62e4"
newsapi = NewsApiClient(api_key=news_api_key)

def extract_news_date():
    try:
        top_headlines = newsapi.get_top_headlines(q='doge', language='en')
        articles = top_headlines['articles']
        logging.info("Extracted news")
        news = []
        for article in articles:
            news.append([article['title'], article['description'], article['url']])
        return news
    except:
        logging.error("Error in extracting news")
        return None
    
articles = extract_news_date()

print(articles[:5])