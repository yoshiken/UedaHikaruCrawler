import twitter
import read_env as env


print (env.tw_token)

auth = twitter.OAuth(token = env.tw_token,
                     token_secret = env.tw_token_secret,
                     consumer_key = env.tw_consumer_key,
                     consumer_secret = env.tw_consumer_secret
                     )

t = twitter.Twitter(auth=auth)

tweets = t.statuses.user_timeline(screen_name="uedakousiki"))
