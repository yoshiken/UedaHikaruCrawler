# -*- coding: utf-8 -*-

from flask import Flask, render_template
from app import read_db

app = Flask(__name__,
            static_folder = "./www/",
            template_folder = "./www")

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")
