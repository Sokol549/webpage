from bs4 import BeautifulSoup
from datetime import datetime,timedelta
import locale
import platform

from webapp.news.parsers.utils import get_html, save_ranobe
from webapp.model import db
from webapp.news.models import News

#if platform.system() == 'Windows':
    #locale.setlocale(locale.LC_ALL, 'russian')
#else:
    #locale.setlocale(locale.LC_TIME, 'ru_RU')


def ranobe_pars():
    html = get_html("https://ранобэ.рф/")
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        news_list = soup.find('div', class_='xs:m-4 sm:m-6 mb-6').findAll('div', class_='xs:max-h-[235px] xs:h-[235px] md:max-h-[300px] md:h-[300px] flex flex-row overflow-hidden')
        result_news = []
        for news in news_list:
            try:
                title = news.find('a', 
                class_='text-black-0 dark:text-grayNormal-200 hover:text-primary cursor-default md:cursor-pointer dark:hover:text-primary xs:text-xl sm:text-2xl md:text-3xl flex-shrink-0 font-bold truncate xs:mb-0 md:mb-1'
                ).text
                
                url_main = 'https://ранобэ.рф' + news.find('a', 
                class_='text-black-0 dark:text-grayNormal-200 hover:text-primary cursor-default md:cursor-pointer dark:hover:text-primary xs:text-xl sm:text-2xl md:text-3xl flex-shrink-0 font-bold truncate xs:mb-0 md:mb-1'
                )['href']
                
                url_chapter = 'https://ранобэ.рф' + news.find('a', 
                class_='flex items-center group my-1 cursor-default lg:cursor-pointer'
                )['href']

            except :
                continue
            save_ranobe(title, url_main, url_chapter)

def get_news_content():
    news_witout_text = News.query.filter(News.text.is_(None))
    for news in news_witout_text:
        html = get_html(news.url)
        if html:
            try:
                soup = BeautifulSoup(html, 'html.parser')
                article = soup.find('div', class_='article-formatted-body article-formatted-body_version-2').decode_contents()
            except :
                continue
            if article:
                news.text = article
                db.session.add(news)
                db.session.commit()

ranobe_pars()