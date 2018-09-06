import feedparser
from pyquery import PyQuery as pq
from insertDB import connectionsql
import dateutil.parser
from datetime import datetime


class News:
    def __init__(self):
        self.res = feedparser.parse('https://news.google.com/news/rss/search/section/q/%E6%A4%8D%E7%94%B0%E3%81%B2%E3%81%8B%E3%82%8B/%E6%A4%8D%E7%94%B0%E3%81%B2%E3%81%8B%E3%82%8B?ned=jp&gl=JP&hl=ja')

    def __getNewsImageURL(self, summary):
        newstext = pq(summary)
        newsimg = newstext('img')
        return newsimg.attr('src')

    def getNews(self, cur):
        news = [[] for i in range(len(self.res['entries']))]
        infotmp = {}
        for i, info in enumerate(self.res['entries']):
            infotmp.clear()
            infotmp['title'] = info['title']
            infotmp['link'] = info['link']
            infotmp['imgurl'] = self.__getNewsImageURL(info['summary'])
            infotmp['updatetime'] = dateutil.parser.parse(info['published'])
            self.update_news(infotmp['title'], infotmp['link'], infotmp['imgurl'], infotmp['updatetime'], cur)
        return news

    def update_news(self, title, link, imgurl, updatetime, cur):
        cur.execute('SELECT * FROM news WHERE title = %s AND link = %s', (title, link))
        if cur.fetchone():
            return
        else:
            cur.execute('INSERT INTO news (title, link, imgurl, updatetime) VALUES (%s,%s,%s,%s);', (title, link, imgurl, updatetime))

    def news(self):
        cur, conn = connectionsql.openConnection()
        self.getNews(cur)
        connectionsql.closeConnection(cur, conn)


if __name__ == '__main__':
    News().news()
    print(datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
