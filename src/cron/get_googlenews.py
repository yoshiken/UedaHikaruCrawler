import feedparser
from pyquery import PyQuery as pq
from insertDB import connectionsql
import dateutil.parser
from datetime import datetime


class News:
    def __init__(self):
        self.res = feedparser.parse('https://news.google.com/news/rss/search/section/q/%E6%A4%8D%E7%94%B0%E3%81%B2%E3%81%8B%E3%82%8B/%E6%A4%8D%E7%94%B0%E3%81%B2%E3%81%8B%E3%82%8B?ned=jp&gl=JP&hl=ja')

    def __getNewsImageURL(self):
        newstext = pq(self.res['entries'][0]['summary'])
        newsimg = newstext('img')
        return newsimg.attr('src')

    def getNews(self):
        news = {}
        news['title'] = self.res['entries'][0]['title']
        news['link'] = self.res['entries'][0]['link']
        news['imgurl'] = self.__getNewsImageURL()
        news['updatetime'] = dateutil.parser.parse(self.res['entries'][0]['published'])
        return news

    def update_news(self, title, link, imgurl, updatetime, cur):
        cur.execute('SELECT * FROM news WHERE title = %s AND link = %s', (title, link))
        if cur.fetchone():
            return
        else:
            cur.execute('INSERT INTO news (title, link, imgurl, updatetime) VALUES (%s,%s,%s,%s);', (title, link, imgurl, updatetime))

    def news(self):
        cur, conn = connectionsql.openConnection()
        newsinfo = self.getNews()
        self.update_news(newsinfo['title'], newsinfo['link'], newsinfo['imgurl'], newsinfo['updatetime'], cur)
        connectionsql.closeConnection(cur, conn)


if __name__ == '__main__':
    News().news()
    print(datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
