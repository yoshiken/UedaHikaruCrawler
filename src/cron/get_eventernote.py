from pyquery import PyQuery as pq
import re


class Event:
    # TODO resがeventでまとまってるのでいちいち全文からParseする必要がない
    def __getEventernoteHTML(self):
        return pq(url='https://www.eventernote.com/actors/9735/events?limit=1000000')

    def __getEventDate(self, res):
        datetext = res('body > div.container > div > div.span8.page > div.gb_event_list.clearfix')('.date').text()
        datepattern = r'\d{4}-\d{2}-\d{2}'
        return re.findall(datepattern, datetext)

    def __getEventTitle(self, res, eventcount):
        title = []
        for ec in range(eventcount):
            title.append(res('body > div.container > div > div.span8.page > div.gb_event_list.clearfix > ul > li:nth-child(' + str(ec) + ') > div.event > h4').text().replace('\u3000', ' '))
        del title[0]
        return title

    def __getEventTime(self, res, eventcount):
        doortime = []
        showtime = []
        closetime = []
        for ec in range(1, eventcount):
            timetext = res('body > div.container > div > div.span8.page > div.gb_event_list.clearfix > ul > li:nth-child(' + str(ec) + ')')('.place').text()
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

    def __getLocation(self, res, eventcount):
        location = []
        for ec in range(eventcount):
            locationtext = (res('body > div.container > div > div.span8.page > div.gb_event_list.clearfix > ul > li:nth-child(' + str(ec) + ') > div.event > div:nth-child(2)').text())
            location.append(locationtext.replace('会場: ', ''))
        del location[0]
        return location

    def __getEventlist(self):
        res = self.__getEventernoteHTML()
        datelist = self.__getEventDate(res)
        eventcount = len(datelist)
        titlelist = self.__getEventTitle(res, eventcount)
        doortimelist, showtimelist, closetimelist = self.__getEventTime(res, eventcount)
        locationlist = self.__getLocation(res, eventcount)
        return eventcount, datelist, titlelist, doortimelist, showtimelist, closetimelist, locationlist

    def getEvents(self):
        eventcount, datelist, titlelist, doortimelist, showtimelist, closetimelist, locationlist = self.__getEventlist()
        events = []
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
