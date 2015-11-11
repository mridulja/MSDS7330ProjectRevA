# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 16:18:31 2015

@author: emrijai
"""

import tweepy
import time
import os, sys


path = 'C:/Mridul/Personal/Masters/Study Material and Resources/MS7330/Project/test'
os.chdir(path)

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey = 'G2HLKdoD6ETrIbRgG0Di1Tc1X'
csecret = 'PWeToU5Ut7oP694VrgaXY1Jb4NOMPA9qQtJ3ih9zx3Xn9WloJr'
atoken = '416373829-GaNjGlK5G4V1NJQfVe5AmIpakNAHADrfIo6cbXTO'
asecret = 'rYYnOtuC31Is5MMztEKUfQbRMICslq6HPn8hCH04IQ5WM'

class listener (StreamListener):
    def on_data(self,data):
        try:
            print data
            saveFile = open('twitterDB.csv','a')
            saveFile.write(data)
            saveFile.write('\n')
            saveFile.close()
            return True
        except BaseException, e:
            print 'Failed OnData : '+ str(e)
            time.sleep(5)
    def on_error(self, status):
        print status
        
auth = OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)
twitterStream=Stream(auth,listener())
twitterStream.filter(track=["#NFL"])