import psycopg2
import os


class readInfo:
    def __init__(self):
        pghost = os.environ['PGHOST']
        pguser = os.environ['PGUSER']
        pgpassword = os.environ['PGPASSWORD']
        pgport = os.environ['PGPORT']
        self.dsn = 'postgresql://' + pguser + ':' + pgpassword + '@' + pghost + ':' + str(pgport) + '/' + pguser
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
