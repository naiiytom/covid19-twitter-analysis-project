from src.secret import key
import tweepy
from src import tweet_streaming

oauth2 = tweet_streaming.connect_twitter(key.api_key, key.api_secret_key, key.access_token, key.access_token_secret)
tracks = ['#โควิท19', '#โควิด19', 'โควิด', 'โควิท']
streamListener = tweet_streaming.MyCustomListener()
myStream = tweepy.Stream(auth=oauth2.auth, listener=streamListener, timeout=30)
tweet_streaming.start_stream(myStream, track=tracks, is_async=True)