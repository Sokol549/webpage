import requests
from bs4 import BeautifulSoup


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
            result_news.append({
                'title':title,
                'url':url,
                'published':published
            })
        return result_news
    return False

