import urllib.parse
import urllib.request
import json
import read_env as env


def dataGet():
    url = 'https://newsapi.org/v2/everything?'
    param = {
        'q': '植田ひかる',
        'apiKey': env.news_apikey
    }
    paramStr = urllib.parse.urlencode(param)
    readObj = urllib.request.urlopen(url + paramStr)
    response = readObj.read()
    return json.loads(response)
