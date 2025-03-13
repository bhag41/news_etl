import pandas as pd
import sqlite3
import logging
from newsapi import NewsApiClient

news_api_key = "10e55a1639ed4d509b1f3f0dbf1b62e4"
newsapi = NewsApiClient(api_key=news_api_key)

