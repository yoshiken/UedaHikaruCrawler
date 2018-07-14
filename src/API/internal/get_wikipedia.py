import requests


def getWikipedeiaLastId():
    # Get latest ID
    res = requests.get('https://ja.wikipedia.org/w/api.php?format=json&action=query&prop=revisions&titles=%E6%A4%8D%E7%94%B0%E3%81%B2%E3%81%8B%E3%82%8B').json()
    # 3589550は植田ひかるさんのページの固有IDっぽい？
    return (res['query']['pages']['3589550']['revisions'][0]['revid'])


def getWikipediaContent():
    # Get Wikideia Text
    res = requests.get('https://ja.wikipedia.org/w/api.php?format=json&action=query&prop=revisions&titles=%E6%A4%8D%E7%94%B0%E3%81%B2%E3%81%8B%E3%82%8B&rvprop=content').json()
    # TODO format json
    return(res['query']['pages']['3589550']['revisions'][0]['*'])
