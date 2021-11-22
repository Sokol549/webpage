import requests


from webapp.model import db
from webapp.news.models import News, Ranobe

def get_html(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:65.0) Gecko/20100101 Firefox/65.0'}
    try:
        result = requests.get(url,headers=headers)
        result.raise_for_status()
        return result.text
    except(requests.RequestException,ValueError):
        print('Ошибка доступа к сайту')
        return False

def save_news(title, url, published):
    news_exist = News.query.filter(News.url == url).count()
    if not news_exist:
        new_news = News(title=title, url=url, published=published)
        db.session.add(new_news)
        db.session.commit()

def save_ranobe(title, url_main, url_chapter):
    ranobe_exist = Ranobe.query.filter(Ranobe.url_chapter == url_chapter).count()
    if not ranobe_exist:
        new_ranobe = Ranobe(title=title, url_chapter=url_chapter, url_main=url_main)
        db.session.add(new_ranobe)
        db.session.commit()