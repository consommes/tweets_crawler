# -*- coding: utf-8 -*-
import tweepy
import os
import importlib,sys

importlib.reload(sys)

consumer_key = '[consumer_key]'
consumer_secret = '[consumer_secret]'
access_token = '[access_token]'
access_token_secret= '[access_token_secret]'

keyword = "Keyword"  

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)  

location = "%s,%s,%s" % ("35.95", "128.25", "10000km") #latitude, logitude, range(km)
                             
wfile = open(os.getcwd()+"/tweets.txt", mode='w', encoding = 'utf-8')        

cursor = tweepy.Cursor(api.search_tweets,
                       q=keyword,
                       since='2021-08-01', #since YYYY-MM-DD
                       count=2000, #tweets per page
                       include_entities=True)

for i, tweet in enumerate(cursor.items()):
    print("{}: {}".format(i, tweet.text))
    wfile.write("{}: {}".format(i, tweet.text) + '\n')
wfile.close()