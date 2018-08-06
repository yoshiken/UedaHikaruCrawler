# -*- coding: utf-8 -*-

from sanic import Sanic
from sanic import response
from app import read_db

app = Sanic()

@app.route("/")
async def index(request):
    app = Sanic()
    Events, News = read_db.readInfo().readAll()

# TODO ちゃんとjsonで返したい
@app.route("/api/events")
async def apiEvents(request):
    app = Sanic()
    Events = read_db.readInfo().readEvent()
    return response.text(Events)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
