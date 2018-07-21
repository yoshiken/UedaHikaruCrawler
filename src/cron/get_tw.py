import json
from requests_oauthlib import OAuth1Session
import get_env as env


class Tweet:
    def getTweets(self):
        twitter = OAuth1Session(env.tw_consumer_key, env.tw_consumer_secret, env.tw_token, env.tw_token_secret)
        url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
        params = {
            "screen_name": "uedakousiki",
            "tweet_mode": "extended"
        }
        res = twitter.get(url, params=params)
        resjson = json.loads(res.text)
        return created_at, id, full_text, retweeted, in_reply_to_status_id, in_reply_to_user_id
