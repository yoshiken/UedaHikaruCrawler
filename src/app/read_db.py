# -*- coding: utf-8 -*-
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

    def readEvent(self):
        self.cur.execute('SELECT * FROM event ORDER BY day DESC')
        res = self.cur.fetchall()
        dict_res = []
        for row in res:
            # @TODO lamdaで辞書全部にNone = 未定をやる
            if row['day'] is not None:
                row['day'] = row['day'].strftime('%Y/%m/%d')
            # @TODO lamda使ってdatatatimeだったら変換
            if row['doortime'] is not None:
                row['doortime'] = row['doortime'].strftime('%H:%M')
            else:
                row['doortime'] = "未定"
            if row['showtime'] is not None:
                row['showtime'] = row['showtime'].strftime('%H:%M')
            else:
                row['showtime'] = "未定"
            if row['closetime'] is not None:
                row['closetime'] = row['closetime'].strftime('%H:%M')
            else:
                row['closetime'] = "未定"
            if row['location'] is None:
                row['location'] = "未定"
            dict_res.append(dict(row))
        return dict_res

    def readNews(self):
        self.cur.execute('SELECT * FROM news ORDER BY updatetime  DESC')
        res = self.cur.fetchall()
        dict_res = []
        for row in res:
            if row['updatetime'] is not None:
                row['updatetime'] = row['updatetime'].isoformat()
            dict_res.append(dict(row))
        return dict_res

    def readNextEvent(self):
        self.cur.execute('SELECT * FROM event WHERE day >= CURRENT_DATE ORDER BY day, showtime')
        res = self.cur.fetchall()
        dict_res = []
        for row in res:
            if row['location'] is None:
                row['location'] = "未定"
            if row['showtime'] is not None:
                row['showtime'] = row['showtime'].strftime('%H:%M')
            dict_res.append(dict(row))
        return dict_res

    def readAll(self):
        return self.readEvent(), self.readNews()
