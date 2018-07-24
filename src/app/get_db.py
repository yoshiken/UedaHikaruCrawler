import psycopg2


class getInfo:
    def __init__(self):
        self.dsn = 'postgresql://ueda:hikaru@postgres:5432/ueda'
        self.conn = psycopg2.connect(self.dsn)
        self.cur = self.conn.cursor()

    def get_event(self):
        self.cur.execute('SELECT * FROM event')
        return self.cur.fetchall()

    def get_news(self):
        self.cur.execute('SELECT * FROM news')
        return self.cur.fetchall()

    def get_wikipedia(self):
        self.cur.execute('SELECT * FROM wikipedi')
        return self.cur.fetchall()

    def get_all(self):
        return self.get_event(), self.get_news(), self.get_wikipedia()
