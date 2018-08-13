# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, jsonify
from app import read_db

app = Flask(__name__,
            static_folder = "./www/static",
            template_folder = "./www")

## JSON日本語文字化け対策
app.config['JSON_AS_ASCII'] = False
app.config["JSON_SORT_KEYS"] = False

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")

@app.route('/api/events')
def catch_apiEvents():
    Events = read_db.readInfo().readEvent()
    return jsonify({
        'status':'200',
        'events':Events
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0')
