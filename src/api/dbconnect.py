# -*- coding: utf-8 -*-
import psycopg2
import psycopg2.extras
import os
from datetime import date, time


class dbBase:
    def __init__(self):
        pghost = os.environ['PGHOST']
        pguser = os.environ['PGUSER']
        pgpassword = os.environ['PGPASSWORD']
        pgport = os.environ['PGPORT']
        self.dsn = 'postgresql://' + pguser + ':' + pgpassword + '@' + pghost + ':' + str(pgport) + '/' + pguser
        self.conn = psycopg2.connect(self.dsn)
        self.cur = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    def get_dict_resultset(self, sql):
        self.cur.execute(sql)
        results = self.cur.fetchall()
        dict_result = []
        for row in results:
            dict_result.append(dict(row))
        return dict_result

    def decodeToStringFomat(self, mix):
        if isinstance(mix, date):
            return mix.strftime('%Y/%m/%d')
        if isinstance(mix, time):
            return mix.strftime('%H:%M')
        if mix is None:
            return mix
        return mix
