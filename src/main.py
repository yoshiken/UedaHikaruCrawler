# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, jsonify
from app import read_db

app = Flask(__name__)

## JSON日本語文字化け対策
app.config['JSON_AS_ASCII'] = False
app.config["JSON_SORT_KEYS"] = False

@app.route('/')
def catch_all():
    return render_template("index.html")

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
