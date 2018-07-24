from sanic import Sanic
from sanic.response import json
from app import get_db

app = Sanic()
Events, News = get_db.getInfo().getAll()


@app.route("/")
async def test(request):
    return json({"hello": "world"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
