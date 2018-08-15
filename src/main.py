# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, jsonify
from app import read_db

app = Flask(__name__)

## JSON日本語文字化け対策
app.config['JSON_AS_ASCII'] = False
app.config["JSON_SORT_KEYS"] = False

app.config['DEBUG'] = True

@app.route('/')
def catch_all():
    Events = read_db.readInfo().readEvent()
    News = read_db.readInfo().readNews()
    return render_template("index.html")

@app.route('/events')
def catch_event():
    Events = read_db.readInfo().readEvent()
    return render_template("events.html")

@app.route('/news')
def catch_news():
    Events = read_db.readInfo().readEvent()
    return render_template("news.html")

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
        'status':'200',
        'events':Events
    })

@app.route('/api/news')
def catch_apiNews():
    News = read_db.readInfo().readNews()
    return jsonify({
        'status':'200',
        'news':News
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0')
