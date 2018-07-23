from sanic import Sanic
from sanic.response import json
from app import playmaker

app = Sanic()

Events, News, Wikipedia = playmaker().info().readAllInfo()

print(Events)


@app.route("/")
async def test(request):
    return json({"hello": "world"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
