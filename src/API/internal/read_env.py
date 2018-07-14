import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

tw_token = os.environ.get('TW_ACCESS_TOKEN')
tw_token_secret = os.environ.get('TW_ACCESS_TOKEN_SECRET')
tw_consumer_key = os.environ.get('TW_CONSUMER_KEY')
tw_consumer_secret = os.environ.get('TW_CONSUMER_SECRET_KEY')
news_apikey = os.environ.get('GOOGLE_NEWS_APIKEY')
