from secret import key
import tweepy

auth = tweepy.OAuthHandler(key.api_key, key.api_secret_key)
