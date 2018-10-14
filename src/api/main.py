from sanic import Sanic, response
from events import ReadEvents
import json

app = Sanic()


@app.route('/')
async def test(request):
    return response.json({'hello': 'world'})


@app.route('/events')
async def get_events(request):
    if eventArgsValidation(request.args):
        return response.json(errorResponse('Validation'))
    params = eventArgsParse(request.args)
    return response.text(eventsSwitch(params))


def eventArgsParse(args):
    params = {'human': 'False', 'ordertype': 'DESC'}
    if not args:
        return params
    for k, v in args.items():
        params[k] = v[0]
    return params


def eventsSwitch(params):
    eventModel = ReadEvents()
    if params['human'] == 'true':
        return json.dumps(eventModel.allEvents(), ensure_ascii=False, indent=4)
    if params['ordertype'] == 'ASC':
        return json.dumps(eventModel.allEvents(), ensure_ascii=False)
    return json.dumps(eventModel.allEvents(), ensure_ascii=False)


def eventArgsValidation(args):
    validationCollection = {'human': ['true', 'false'], 'ordertype': ['ASC', 'DESC']}
    if not args:
        return False
    for param in args:
        if args[param][0] not in validationCollection[param]:
            return True
    return False


def errorResponse(errorStatus):
    response = {'status': 400}
    errorDetail = {
        'Validation': 'Validation Error'
    }
    try:
        response['body'] = {'error detail': errorDetail[errorStatus]}
    except KeyError:
        response['body'] = 'Unknown error'
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1337)
