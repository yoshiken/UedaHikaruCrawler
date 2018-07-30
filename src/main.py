from sanic import Sanic
from sanic.response import json
from app import read_db


@app.route("/")
async def index(request):
    app = Sanic()
    Events, News = read_db.readInfo().readAll()
    return uri_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
