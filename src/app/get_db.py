import psycopg2


dsn = 'postgresql://ueda:hikaru@postgres:5432/ueda'
conn = psycopg2.connect(dsn)
cur = conn.cursor()


class getDBEvent:

    def get_all(self):
        cur.execute('SELECT * FROM event')
        return cur.fetchall()


class getDBNews:

    def get_all(self):
        cur.execute('SELECT * FROM news')
        return cur.fetchall()


class getDBWikipedia:

    def get_all(self):
        cur.execute('SELECT * FROM wikipedia')
        return cur.fetchall()
