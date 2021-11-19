import requests
from bs4 import BeautifulSoup
from datetime import datetime
from webapp.model import db, News


def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException,ValueError):
        print('ERROR')
        return False

def get_python_news():
    html = get_html("https://www.python.org/blogs/")
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        news_list = soup.find('ul', class_='list-recent-posts').findAll('a')
        result_news = []
        for news in news_list:
            title = news.text
            url= news['href']
            published = news.findNext('time').text
            try:
                published = datetime.strptime(published,'%Y-%m-%d')
            except(ValueError):
                published = datetime.now()
            result_news.append({
                'title':title,
                'url':url,
                'published':published
            })
            save_news(title, url, published)
    return False

def save_news(title, url, published):
    news_exist = News.query.filter(News.url == url).count()
    if not news_exist:
        new_news = News(title=title, url=url, published=published)
        db.session.add(new_news)
        db.session.commit()
