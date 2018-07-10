import requests

# Get latest ID
r = requests.get('https://ja.wikipedia.org/w/api.php?format=json&action=query&prop=revisions&titles=%E6%A4%8D%E7%94%B0%E3%81%B2%E3%81%8B%E3%82%8B').json()
print(r['query']['pages']['3589550']['revisions'][0]['revid'])
