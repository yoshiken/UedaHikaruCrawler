import psycopg2
import os


class connectionsql:
    @classmethod
    def openConnection(self):
        pghost = os.environ['PGHOST']
        pguser = os.environ['PGUSER']
        pgpassword = os.environ['PGPASSWORD']
        pgport = os.environ['PGPORT']
        dsn = 'postgresql://' + pguser + ':' + pgpassword + '@' + pghost + ':' + str(pgport) + '/' + pguser
        conn = psycopg2.connect(dsn)
        cur = conn.cursor()
        return cur, conn

    @classmethod
    def closeConnection(self, cur, conn):
        conn.commit()
        cur.close()
        conn.close()
        return
