import feedparser
from PIL import Image
import requests



class NewsScraper:
    def __init__(self):
        self.name = "Quillings"

        
    def parse_feed(self, link="https://www.wired.com/feed/rss"):
        link = "https://www.wired.com/feed/rss"
        feed = feedparser.parse(link)

        posts = []

        for entry in feed.entries:
            
            title = entry.title
            image_url = entry.media_thumbnail[0]['url']
            date = entry.published
            post = {'title': title, 'image_url': image_url, 'date': date}
            posts.append(post)

        return posts
