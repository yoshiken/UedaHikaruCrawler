from sanic import Sanic, response
from events import ReadEvents
import json

app = Sanic()


@app.route('/')
async def test(request):
    return response.json({'hello': 'world'})


@app.route('/events')
async def get_events(request):
    return response.text(eventsSwitch(request.args))


def eventsSwitch(args):
    eventModel = ReadEvents()
    if not args:
        return json.dumps(eventModel.allEvents(), ensure_ascii=False)
    if args['human'][0] == 'true':
        return json.dumps(eventModel.allEvents(), ensure_ascii=False, indent=4)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1337)
