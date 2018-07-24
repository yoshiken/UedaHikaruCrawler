import psycopg2


class readInfo:
    def __init__(self):
        # TODO 本番用にenvか環境変数呼ぶ
        self.dsn = 'postgresql://ueda:hikaru@postgres:5432/ueda'
        self.conn = psycopg2.connect(self.dsn)
        self.cur = self.conn.cursor()

    def readEvent(self):
        self.cur.execute('SELECT * FROM event')
        return self.cur.fetchall()

    def readNews(self):
        self.cur.execute('SELECT * FROM news')
        return self.cur.fetchall()

    def readAll(self):
        return self.readEvent(), self.readNews()
