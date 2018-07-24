import psycopg2


class getInfo:
    def __init__(self):
        self.dsn = 'postgresql://ueda:hikaru@postgres:5432/ueda'
        self.conn = psycopg2.connect(self.dsn)
        self.cur = self.conn.cursor()

    def getEvent(self):
        self.cur.execute('SELECT * FROM event')
        return self.cur.fetchall()

    def getNews(self):
        self.cur.execute('SELECT * FROM news')
        return self.cur.fetchall()

    def getWikipedia(self):
        self.cur.execute('SELECT * FROM wikipedi')
        return self.cur.fetchall()

    def getAll(self):
        return self.getEvent(), self.getNews(), self.getWikipedia()
