# -*- coding: utf-8 -*-
"""
Created on Wed Aug 20 15:43:21 2014

"""

#from tweepy import Stream
#from tweepy import OAuthHandler
#from tweepy.streaming import StreamListener
#from tweepy import retweet
import tweepy
import time
import json

cKey = ''
cSecret = ''
aToken = ''
aSecret = ''
 
class listener(tweepy.StreamListener):
    def on_data(self, data):
        try:
            jsonInput = data
            decoded = json.loads(jsonInput)
            
            rtCount = decoded['retweeted_status']['retweet_count']
            print rtCount
            if rtCount > 4:
                api = tweepy.API(auth)
                saveThis = data
                storeFile = open('path', 'a')
                storeFile.write(saveThis)
                storeFile.write('\n')
                storeFile.close()
                tweetID = decoded['retweeted_status']['id']
                api.retweet(tweetID)        
            
            return True
        except BaseException, e:
            print 'failed ondata,', str(e)
            time.sleep(5)
    def on_error(self, status):
        print status
        
auth = tweepy.OAuthHandler(cKey, cSecret)
auth.set_access_token(aToken, aSecret)
twitterStream = tweepy.Stream(auth, listener())
twitterStream.filter(track=["KEYWORD"]) 
