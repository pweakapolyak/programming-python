import feedparser
from utils import translate_html
from datetime import datetime
from story import NewsStory


def read_latest_news(url):
    """
    Read RSS-news from url
    :param url: url of rss-server
    :type url: str
    :return: list[NewsStory]
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    result = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        news_story = NewsStory(guid, title, description, link, pubdate)
        result.append(news_story)
    return result
