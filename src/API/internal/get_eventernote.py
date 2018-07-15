from pyquery import PyQuery as pq
import re


def __getEventernoteHTML():
    return pq(url='https://www.eventernote.com/actors/9735/events?limit=1000000')


def getEventDate(res):
    datetext = res('body > div.container > div > div.span8.page > div.gb_event_list.clearfix')('.date').text()
    datepattern = r'\d{4}-\d{2}-\d{2}'
    return re.findall(datepattern, datetext)


def getEventTitle(res, eventcount):
    title = []
    for ec in range(eventcount):
        title.append(res('body > div.container > div > div.span8.page > div.gb_event_list.clearfix > ul > li:nth-child(' + str(ec) + ') > div.event > h4').text().replace('\u3000', ' '))
    del title[0]
    return title


def getEventTime(res, eventcount):
    timetext = res('body > div.container > div > div.span8.page > div.gb_event_list.clearfix')('.place').text()
    timepattern = r'\d{2}:\d{2}|-'
    alltimedata = re.findall(timepattern, timetext)
    doortime = []
    showtime = []
    closetime = []
    for ec in range(eventcount * 3):
        if(ec == 0 or ec % 3 == 0):
            doortime.append(alltimedata[ec])
        elif(ec % 3 == 1):
            showtime.append(alltimedata[ec])
        else:
            closetime.append(alltimedata[ec])
    return doortime, showtime, closetime


def getLocation(res, eventcount):
    location = []
    for ec in range(eventcount):
        locationtext = (res('body > div.container > div > div.span8.page > div.gb_event_list.clearfix > ul > li:nth-child(' + str(ec) + ') > div.event > div:nth-child(2)').text())
        location.append(locationtext.replace('会場: ', ''))
    del location[0]
    return location


def getEventinfo():
    res = __getEventernoteHTML()
    datelist = getEventDate(res)
    eventcount = len(datelist)
    titlelist = getEventTitle(res, eventcount)
    doortimelist, showtimelist, closetimelist = getEventTime(res, eventcount)
    locationlist = getLocation(res, eventcount)
    return eventcount, datelist, titlelist, doortimelist, showtimelist, closetimelist, locationlist