from pyquery import PyQuery as pq
import re
from insertDB import connectionsql
from datetime import datetime


class Event:
    # TODO resがeventでまとまってるのでいちいち全文からParseする必要がない
    def __init__(self):
        self.res = pq('https://www.eventernote.com/actors/9735/events?limit=1000000')

    def __getEventDate(self):
        datetext = self.res('body > div.container > div > div.span8.page > div.gb_event_list.clearfix')('.date').text()
        datepattern = r'\d{4}-\d{2}-\d{2}'
        return re.findall(datepattern, datetext)

    def __getEventTitle(self, eventcount):
        title = []
        for ec in range(eventcount):
            title.append(self.res('body > div.container > div > div.span8.page > div.gb_event_list.clearfix > ul > li:nth-child(' + str(ec) + ') > div.event > h4').text().replace('\u3000', ' '))
        del title[0]
        return title

    def __getEventTime(self, eventcount):
        doortime = []
        showtime = []
        closetime = []
        for ec in range(1, eventcount):
            timetext = self.res('body > div.container > div > div.span8.page > div.gb_event_list.clearfix > ul > li:nth-child(' + str(ec) + ')')('.place').text()
            timepattern = r'\d{2}:\d{2}|-'
            timedate = re.findall(timepattern, timetext)
            if not timedate:
                doortime.append('-')
                showtime.append('-')
                closetime.append('-')
                continue
            doortime.append(timedate[0])
            showtime.append(timedate[1])
            closetime.append(timedate[2])
        return doortime, showtime, closetime

    def __getLocation(self, eventcount):
        location = []
        for ec in range(eventcount):
            locationtext = (self.res('body > div.container > div > div.span8.page > div.gb_event_list.clearfix > ul > li:nth-child(' + str(ec) + ') > div.event > div:nth-child(2)').text())
            location.append(locationtext.replace('会場: ', ''))
        del location[0]
        return location

    def __getEventlist(self):
        datelist = self.__getEventDate()
        eventcount = len(datelist)
        titlelist = self.__getEventTitle(eventcount)
        doortimelist, showtimelist, closetimelist = self.__getEventTime(eventcount)
        locationlist = self.__getLocation(eventcount)
        return eventcount, datelist, titlelist, doortimelist, showtimelist, closetimelist, locationlist

    def getEvents(self):
        eventcount, datelist, titlelist, doortimelist, showtimelist, closetimelist, locationlist = self.__getEventlist()
        events = []
        # TODO ec使う必要あるか？(index引っ張ってこれそう)
        for ec in range(eventcount - 1):
            events.append({
                "eventcount": ec,
                "date": datelist[ec],
                "title": titlelist[ec],
                "doortime": doortimelist[ec],
                "showtime": showtimelist[ec],
                "closetime": closetimelist[ec],
                "location": locationlist[ec]
            })
        return events

    def isEvent(self, title, cur):
        cur.execute('SELECT * FROM event WHERE title = %s', (title, ))
        rows = cur.fetchone()
        return bool(rows)

    def insertEvent(self, event, cur):
        cur.execute('INSERT INTO event (day, title, location) VALUES (%s, %s, %s);', (event['date'], event['title'], event['location']))

    # TODO もっと頭良くやれそう
    def updateEvent(self, event, cur):
        if event['doortime'] != '-':
            cur.execute('UPDATE event SET doortime = %s WHERE title = %s;', (event['doortime'], event['title']))
        if event['showtime'] != '-':
            cur.execute('UPDATE event SET showtime = %s WHERE title = %s;', (event['showtime'], event['title']))
        if event['closetime'] != '-':
            cur.execute('UPDATE event SET closetime = %s WHERE title = %s;', (event['closetime'], event['title']))

    def event(self):
        cur, conn = connectionsql.openConnection()
        eventList = self.getEvents()
        for event in eventList:
            if not self.isEvent(event['title'], cur):
                self.insertEvent(event, cur)
            self.updateEvent(event, cur)
        connectionsql.closeConnection(cur, conn)


if __name__ == '__main__':
    Event().event()
    print(datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
