# -*- coding: utf-8 -*-

from sanic import Sanic
from sanic import response
from jinja2 import Environment, FileSystemLoader
from app import read_db

env = Environment(loader=FileSystemLoader('/app/src/templates/', encoding='utf8'))
app = Sanic()

@app.route("/")
async def index(request):
    app = Sanic()
    Events, News = read_db.readInfo().readAll()
    tpl = env.get_template('index.html')
    html = tpl.render({'hoge':'hello'})
    return response.html(html)

# TODO ちゃんとjsonで返したい
@app.route("/api/events")
async def apiEvents(request):
    app = Sanic()
    Events = read_db.readInfo().readEvent()
    return response.text(Events)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
