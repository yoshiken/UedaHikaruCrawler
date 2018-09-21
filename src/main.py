# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
from app import read_db
import urllib.parse


app = Flask(__name__, static_folder='static', static_url_path='')

PAGE_DISPLAY = 15


@app.route('/')
def catch_index():
    NextEvents = createGoogleCalendarAddURL(read_db.readInfo().readNextEvent())
    return render_template("index.html", NextEvents=NextEvents)


@app.route('/events')
def catch_event():
    page = request.args.get('page')
    page = 1 if page is None else int(page)
    Events = read_db.readInfo().readEvent()
    page_serial = page * PAGE_DISPLAY
    lastflag = True if int(len(Events) / PAGE_DISPLAY) >= page else False
    Events = Events[page_serial - PAGE_DISPLAY: page_serial]
    return render_template("events.html", Events=Events, page=page, nextpage=page + 1, prevpage=page - 1, lastflag=lastflag)


@app.route('/news')
def catch_news():
    News = read_db.readInfo().readNews()
    return render_template("news.html", News=News)


@app.route('/twitter')
def catch_twitter():
    return render_template("twitter.html")


@app.route('/about')
def catch_about():
    return render_template("about.html")


@app.route('/develop')
def catch_develop():
    return render_template("develop.html")


def createGoogleCalendarAddURL(events):
    for i, event in enumerate(events):
        url = 'http://www.google.com/calendar/event?action=TEMPLATE'
        url += '&text=' + urllib.parse.quote(event['title'])
        if (event['day'] is not None and event['showtime'] is not None and event['closetime'] is not None):
            url += '&dates=' + event['day'].strftime('%Y%m%d') + 'T' + event['showtime'].replace(":", "") + '00/' + event['day'].strftime('%Y%m%d') + 'T' + event['closetime'].strftime('%H%M%S')
        if (event['location'] is not None):
            url += '&location=' + urllib.parse.quote(event['location'])
        event['addccalendaurl'] = url
    return events


if __name__ == "__main__":
    app.run(host='0.0.0.0')
