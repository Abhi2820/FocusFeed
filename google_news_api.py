'''

import requests
import sys
import os

# Add the root directory to sys.path so that config.py can be found
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from config import API_KEY  # Corrected import

def fetch_articles():
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}&pageSize=50"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        articles = data.get("articles", [])
        print("Fetched articles:", articles)
        return articles
    else:
        print("Failed to fetch articles:", response.status_code)
        return []


'''
import requests
import sys
import os

# Add the root directory to sys.path so that config.py can be found
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from config import API_KEY  # Corrected import

def fetch_articles(preferences):
    base_url = "https://newsapi.org/v2/top-headlines"
    articles = []

    for category in preferences:
        response = requests.get(
            base_url,
            params={
                "apiKey": API_KEY,
                "country": "us",
                "category": category.lower(),
                "pageSize": 50
            }
        )
        if response.status_code == 200:
            data = response.json()
            articles.extend(data.get("articles", []))
        else:
            print(f"Failed to fetch articles for {category}: {response.status_code}")

    return articles[:50]  # Limit to 50 articles
