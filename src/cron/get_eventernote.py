from pyquery import PyQuery as pq
import re
from insertDB import connectionsql
from datetime import datetime
import requests


class Event:
    # TODO resがeventでまとまってるのでいちいち全文からParseする必要がない
    def __init__(self):
        self.res = pq('https://www.eventernote.com/actors/9735/events?limit=1000000&sort=event_date&order=ASC')

    def __getEventDate(self):
        datetext = self.res('body > div.container > div > div.span8.page > div.gb_event_list.clearfix')('.date').text()
        datepattern = r'\d{4}-\d{2}-\d{2}'
        return re.findall(datepattern, datetext)

    def __getEventTitle(self, eventcount):
        title = []
        for ec in range(1, eventcount + 1):
            title.append(self.res('body > div.container > div > div.span8.page > div.gb_event_list.clearfix > ul > li:nth-child(' + str(ec) + ') > div.event > h4').text().replace('\u3000', ' '))
        return title

    def __getEventTime(self, eventcount):
        doortime = []
        showtime = []
        closetime = []
        for ec in range(1, eventcount + 1):
            timetext = self.res('body > div.container > div > div.span8.page > div.gb_event_list.clearfix > ul > li:nth-child(' + str(ec) + ')')('.place').text()
            timepattern = r'\d{2}:\d{2}|-'
            timedate = [None if i is '-' else i for i in re.findall(timepattern, timetext)]
            doortime.append(timedate[0])
            showtime.append(timedate[1])
            closetime.append(timedate[2])
        return doortime, showtime, closetime

    def __getLocation(self, eventcount):
        location = []
        for ec in range(1, eventcount + 1):
            locationtext = (self.res('body > div.container > div > div.span8.page > div.gb_event_list.clearfix > ul > li:nth-child(' + str(ec) + ') > div.event > div:nth-child(2)').text())
            location.append(locationtext.replace('会場: ', ''))
        return location

    def __getEventlist(self):
        datelist = self.__getEventDate()
        eventcount = len(datelist)
        titlelist = self.__getEventTitle(eventcount)
        doortimelist, showtimelist, closetimelist = self.__getEventTime(eventcount)
        locationlist = self.__getLocation(eventcount)
        imgnamelist = self.getEventsImg(eventcount)
        return eventcount, datelist, titlelist, doortimelist, showtimelist, closetimelist, locationlist, imgnamelist

    def getEvents(self):
        eventcount, datelist, titlelist, doortimelist, showtimelist, closetimelist, locationlist, imgnamelist = self.__getEventlist()
        events = []
        # TODO ec使う必要あるか？(index引っ張ってこれそう)
        for ec in range(eventcount):
            events.append({
                "eventid": ec,
                "date": datelist[ec],
                "title": titlelist[ec],
                "doortime": doortimelist[ec],
                "showtime": showtimelist[ec],
                "closetime": closetimelist[ec],
                "location": locationlist[ec],
                "imgname": imgnamelist[ec]
            })
        return events

    def getEventsImg(self, eventcount):
        filenames = []
        for ec in range(1, eventcount + 1):
            imgURL = (self.res('body > div.container > div > div.span8.page > div.gb_event_list.clearfix > ul > li:nth-child(' + str(ec) + ') > div.date')('img').attr('src'))
            if imgURL is None:
                filenames.append(None)
                continue
            img = requests.get(imgURL)
            filename = imgURL.split('/')[-1]
            filenames.append(filename)
            try:
                with open('/src/app/static/img/event/' + filename, 'wb') as f:
                    f.write(img.content)
            except FileExistsError:
                pass
        return filenames

    def isEvent(self, eventid, cur):
        cur.execute('SELECT * FROM event WHERE eventid = %s', (eventid, ))
        rows = cur.fetchone()
        return bool(rows)

    def insertEvent(self, event, cur):
        cur.execute('INSERT INTO event (day, title, location, imgname) VALUES (%s, %s, %s, %s);', (event['date'], event['title'], event['location'], event['imgname']))

    # TODO もっと頭良くやれそう
    def updateEvent(self, event, cur):
        cur.execute('UPDATE event SET day = %s, title = %s, doortime = %s, showtime = %s, closetime = %s, imgname = %s, location = %s WHERE eventid = %s;', (event['date'], event['title'], event['doortime'], event['showtime'], event['closetime'], event['imgname'], event['location'], event['eventid']))

    def event(self):
        cur, conn = connectionsql.openConnection()
        eventList = self.getEvents()
        for event in eventList:
            if not self.isEvent(event['eventid'], cur):
                self.insertEvent(event, cur)
            self.updateEvent(event, cur)
        connectionsql.closeConnection(cur, conn)


if __name__ == '__main__':
    Event().event()
    print(datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
