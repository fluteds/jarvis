import requests
import feedparser
from config import NEWS_API_KEY

# Function to fetch news headlines
def fetch_news(source_type=None, api_key=None, feed_url=None):
    headlines = []
    if source_type == 'api':
        if api_key:
            url = "https://newsapi.org/v2/top-headlines"
            params = {
                "country": "gb", 
                "apiKey": NEWS_API_KEY
            }

            response = requests.get(url, params=params)
            news_data = response.json()

            if 'articles' in news_data:
                # Limit to 5 headlines
                headlines = [article['title'] for article in news_data['articles'][:5]]
            else:
                headlines = ["Failed to fetch news headlines."]
        else:
            headlines = ["News API key is missing."]
    elif source_type == 'rss': # Default source (api or rss)
        try:
            if feed_url:
                # Parse the RSS feed
                feed = feedparser.parse(feed_url)

                if feed.get('bozo', 0) == 0:
                    # If the feed is successfully parsed without errors
                    # Limit to 5 headlines
                    headlines = [entry.title for entry in feed.entries][:5]
                else:
                    headlines = ["Failed to fetch news headlines. Invalid RSS feed."]
            else:
                headlines = ["RSS feed URL is missing."]
        except Exception as e:
            headlines = ["Failed to fetch news headlines.", str(e)]
    else:
        headlines = ["Invalid source type. Defaulting to using RSS feed."]

        # Example RSS feed URL
        rss_feed_url = "https://feeds.bbci.co.uk/news/world/rss.xml"
        headlines = fetch_news('rss', feed_url=rss_feed_url)

    return headlines
