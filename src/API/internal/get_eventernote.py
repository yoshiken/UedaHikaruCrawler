from pyquery import PyQuery as pq
import re


def __getEventernoteHTML():
    return pq(url='https://www.eventernote.com/actors/9735/events?limit=1000000')


def __getEventDate(res):
    datetext = res('body > div.container > div > div.span8.page > div.gb_event_list.clearfix')('.date').text()
    datepattern = r'\d{4}-\d{2}-\d{2}'
    return re.findall(datepattern, datetext)


def __getEventTitle(res, eventcount):
    title = []
    for ec in range(eventcount):
        title.append(res('body > div.container > div > div.span8.page > div.gb_event_list.clearfix > ul > li:nth-child(' + str(ec) + ') > div.event > h4').text().replace('\u3000', ' '))
    del title[0]
    return title


def __getEventTime(res, eventcount):
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


def __getLocation(res, eventcount):
    location = []
    for ec in range(eventcount):
        locationtext = (res('body > div.container > div > div.span8.page > div.gb_event_list.clearfix > ul > li:nth-child(' + str(ec) + ') > div.event > div:nth-child(2)').text())
        location.append(locationtext.replace('会場: ', ''))
    del location[0]
    return location


def __getEventlist():
    res = __getEventernoteHTML()
    datelist = __getEventDate(res)
    eventcount = len(datelist)
    titlelist = __getEventTitle(res, eventcount)
    doortimelist, showtimelist, closetimelist = __getEventTime(res, eventcount)
    locationlist = __getLocation(res, eventcount)
    return eventcount, datelist, titlelist, doortimelist, showtimelist, closetimelist, locationlist


def getEvents():
    eventcount, datelist, titlelist, doortimelist, showtimelist, closetimelist, locationlist = __getEventlist()
    events = []
    for ec in range(eventcount-1):
        events.append({
        "eventcount":ec,
        "date":datelist[ec],
        "title":titlelist[ec],
        "doortime":doortimelist[ec],
        "showtime":showtimelist[ec],
        "closetime":closetimelist[ec],
        "location":locationlist[ec]
        })
    return events
