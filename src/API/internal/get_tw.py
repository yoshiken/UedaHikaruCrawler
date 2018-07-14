import json
from requests_oauthlib import OAuth1Session
import read_env as env


def getTweets():
    twitter = OAuth1Session(env.tw_consumer_key, env.tw_consumer_secret, env.tw_token, env.tw_token_secret)
    url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
    params = {
        "screen_name": "uedakousiki"
    }
    res = twitter.get(url, params=params)
    return json.loads(res.text)
