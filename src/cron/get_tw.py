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
        return json.loads(res.text)

    def parseTweets(self):
        tweetsjson = self.getTweets()
        withdrawnTweet = []
        for index, tweet in enumerate(tweetsjson):
            withdrawnTweet.append({
                "id": tweetsjson[index]["id"],
                "created_at": tweetsjson[index]["created_at"],
                "text": tweetsjson[index]["full_text"],
                "retweeted": tweetsjson[index]["retweeted"],
                "in_reply_to_status_id": tweetsjson[index]["in_reply_to_status_id"],
                "in_reply_to_user_id": tweetsjson[index]["in_reply_to_user_id"]
            })
        return withdrawnTweet
