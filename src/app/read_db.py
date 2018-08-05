import psycopg2
import psycopg2.extras
import os


class readInfo:
    def __init__(self):
        pghost = os.environ['PGHOST']
        pguser = os.environ['PGUSER']
        pgpassword = os.environ['PGPASSWORD']
        pgport = os.environ['PGPORT']
        self.dsn = 'postgresql://' + pguser + ':' + pgpassword + '@' + pghost + ':' + str(pgport) + '/' + pguser
        self.conn = psycopg2.connect(self.dsn)
        self.cur = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    def get_dict_resultset(sql):
        self.cur.execute (sql)
        results = self.cur.fetchall()
        dict_result = []
        for row in results:
            dict_result.append(dict(row))
        return dict_result

    def readEvent(self):
        self.cur.execute('SELECT * FROM event')
        results = self.cur.fetchall()
        dict_result = []
        for row in results:
            dict_result.append(dict(row))
        return dict_result


    def readNews(self):
        self.cur.execute('SELECT * FROM news')
        return self.cur.fetchall()

    def readAll(self):
        return self.readEvent(), self.readNews()
