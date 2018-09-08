# -*- coding: utf-8 -*-

from flask import Flask, render_template, jsonify
from app import read_db
import urllib.parse


app = Flask(__name__)

# JSON日本語文字化け対策
app.config['JSON_AS_ASCII'] = False
app.config["JSON_SORT_KEYS"] = False

app.config['DEBUG'] = True


@app.route('/')
def catch_index():
    NextEvents = createGoogleCalendarAddURL(read_db.readInfo().readNextEvent())
    return render_template("index.html", NextEvents=NextEvents)


@app.route('/events')
def catch_event():
    Event = read_db.readInfo().readEvent()
    return render_template("events.html", Events=Event)


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


@app.route('/api/events')
def catch_apiEvents():
    Events = read_db.readInfo().readEvent()
    return jsonify({
        'status': '200',
        'events': Events
    })


@app.route('/api/news')
def catch_apiNews():
    News = read_db.readInfo().readNews()
    return jsonify({
        'status': '200',
        'news': News
    })


def createGoogleCalendarAddURL(events):
    base = 'http://www.google.com/calendar/event?action=TEMPLATE'
    for event in events:
        title = '&text=' + urllib.parse.quote(event['title'])
        date = '&dates=' + event['day'].strftime('%Y%m%d') + 'T' + event['showtime'].replace(":", "") + '00/' + event['day'].strftime('%Y%m%d') + 'T' + event['closetime'].strftime('%H%M%S')
        location = '&location=' + urllib.parse.quote(event['location'])
        event['addccalendaurl'] = base + title + date + location
    return events


if __name__ == "__main__":
    app.run(host='0.0.0.0')
