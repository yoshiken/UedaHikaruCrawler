# -*- coding: utf-8 -*-
from dbconnect import dbBase


class ReadEvents(dbBase):
    def allEvents(self, reverse=False):
        sql = 'SELECT eventid, title, day, doortime, showtime, closetime, location FROM event ORDER BY showtime, day '
        ordertype = 'ASC' if reverse else 'DESC'
        sql = sql + ordertype
        result = self.get_dict_resultset(sql)
        stringresult = self.replacementTypeDateToString(result)
        return self.convertToJsonFormat(stringresult)

    def replacementTypeDateToString(self, results):
        string_result = []
        for result in results:
            for k, v in result.items():
                result[k] = v if isinstance(v, str) else self.decodeToStringFomat(v)
            string_result.append(result)
        return string_result

    def convertToJsonFormat(self, results):
        jsonresult = []
        for result in results:
            jsontimebody = {'day': result['day'], 'doortime': result['doortime'], 'showtime': result['showtime'], 'closetime': result['closetime']}
            jsonbody = {'title': result['title'], 'location': result['location'], 'time': jsontimebody}
            jsonresult.append({'eventid': result['eventid'], 'body': jsonbody})
        return jsonresult
