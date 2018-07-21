import requests


class Wikipedia:
    def __getWikipedeiaLastId(self):
        res = requests.get('https://ja.wikipedia.org/w/api.php?format=json&action=query&prop=revisions&titles=%E6%A4%8D%E7%94%B0%E3%81%B2%E3%81%8B%E3%82%8B').json()
        # 3589550は植田ひかるさんのページの固有IDっぽい？
        return (res['query']['pages']['3589550']['revisions'][0]['revid'])

    def __getWikipediaContent(self):
        res = requests.get('https://ja.wikipedia.org/w/api.php?format=json&action=query&prop=revisions&titles=%E6%A4%8D%E7%94%B0%E3%81%B2%E3%81%8B%E3%82%8B&rvprop=content').json()
        return(res['query']['pages']['3589550']['revisions'][0]['*'])

    def getWikipedeia(self):
        revid = {'revid': self.__getWikipedeiaLastId()}
        # TODO convert json
        content = {'content': self.__getWikipediaContent()}
        return revid, content
