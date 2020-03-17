import tweepy
from pymongo import MongoClient
import json


def connect_twitter(api_key: str, api_secret_key: str, access_token: str, access_token_secret: str):
    auth = tweepy.OAuthHandler(api_key, api_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    twitter = tweepy.API(auth, wait_on_rate_limit=True,
                         wait_on_rate_limit_notify=True)
    print(f'connected to twitter')
    return twitter


def connect_database(host='localhost', port=27017):
    client = MongoClient(f'mongodb://{host}:{port}/')
    print(f'connected to: {host} on port {port}')
    return client


def start_stream(stream, **kwargs):
    try:
        stream.filter(**kwargs)
    except Exception as e:
        print(e)
        stream.disconnect()
        print("Fatal Error")


class MyCustomListener(tweepy.StreamListener):
    def __init__(self):
        self.client = connect_database()

    def on_connect(self):
        print(f'Start streaming tweets data...')

    def on_error(self, status_code):
        if(status_code == 420):
            return False

    def on_status(self, status):
        print(status.text)
        return True

    def on_data(self, raw_data):
        try:
            data = json.loads(raw_data)
            if "text" in data:
                tweet_collection = self.client['data_engineer']['tweet']
                tweet_collection.insert(data)
        except Exception as e:
            print('Error:', e)