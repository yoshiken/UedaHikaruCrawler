# -*- coding: utf-8 -*-
import psycopg2
import psycopg2.extras
import os
import json
from datetime import date, datetime

class readInfo:
    def __init__(self):
        pghost = os.environ['PGHOST']
        pguser = os.environ['PGUSER']
        pgpassword = os.environ['PGPASSWORD']
        pgport = os.environ['PGPORT']
        self.dsn = 'postgresql://' + pguser + ':' + pgpassword + '@' + pghost + ':' + str(pgport) + '/' + pguser
        self.conn = psycopg2.connect(self.dsn)
        self.cur = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    def get_dict_resultset(self, sql):
        self.cur.execute (sql)
        results = self.cur.fetchall()
        dict_result = []
        for row in results:
            dict_result.append(dict(row))
        return dict_result

    def readEvent(self):
        self.cur.execute('SELECT * FROM event')
        res = self.cur.fetchall()
        dict_res = []
        for row in res:
            if row['day'] is not None:
                row['day'] = row['day'].strftime('%Y/%m/%d')
            ## @TODO lamda使ってdatatatimeだったら変換
            if row['doortime'] is not None:
                row['doortime'] = row['doortime'].isoformat()
            if row['showtime'] is not None:
                row['showtime'] = row['showtime'].isoformat()
            if row['closetime'] is not None:
                row['closetime'] = row['closetime'].isoformat()
            dict_res.append(dict(row))
        return dict_res

    def readNews(self):
        self.cur.execute('SELECT * FROM news')
        return self.cur.fetchall()

    def readAll(self):
        return self.readEvent(), self.readNews()
