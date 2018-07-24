import psycopg2


class connectionsql:
    @classmethod
    def openConnection(self):
        dsn = 'postgresql://ueda:hikaru@postgres:5432/ueda'
        conn = psycopg2.connect(dsn)
        cur = conn.cursor()
        return cur, conn

    @classmethod
    def closeConnection(self, cur, conn):
        conn.commit()
        cur.close()
        conn.close()
        return
