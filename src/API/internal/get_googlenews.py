import feedparser
import json
from pyquery import PyQuery as pq
import datetime

class News:
    def __getNewsHTML(self):
        url = 'https://news.google.com/news/rss/search/section/q/%E6%A4%8D%E7%94%B0%E3%81%B2%E3%81%8B%E3%82%8B/%E6%A4%8D%E7%94%B0%E3%81%B2%E3%81%8B%E3%82%8B?ned=jp&gl=JP&hl=ja'
        return feedparser.parse(url)

    def __getNewsImageURL(self, res):
        newstext = pq(res)
        newsimg = newstext('img')
        return newsimg.attr('src')

    def __getNewsDate(self, res):
        return datetime.datetime(*res[:6])


    def getNews(self):
        res = self.__getNewsHTML()
        title = {'title': res['entries'][0]['title']}
        link = {'link': res['entries'][0]['link']}
        imgURL = {'imgURL': self.__getNewsImageURL(res['entries'][0]['summary'])}
        updatetime = {'updatetime': self.__getNewsDate(res['entries'][0]['published_parsed'])}
        return title, link, imgURL, updatetime
