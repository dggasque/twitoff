"""Retrieve tweets, embedding, save into database"""

import basilica
import tweepy
from decouple import config
from .models import DB, Tweet, User
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

TWITTER_AUTH = tweepy.OAuthHandler(config('TWITTER_CONSUMER_KEY'),
                                   config('TWITTER_CONSUMER_SECRET'))
TWITTER_AUTH.set_access_token(config('TWITTER_ACCESS_TOKEN'),
                              config('TWITTER_ACCESS_TOKEN_SECRET'))
TWITTER = tweepy.API(TWITTER_AUTH)
BASILICA = basilica.Connection(config('BASILICA_KEY'))

#to do - add functions later