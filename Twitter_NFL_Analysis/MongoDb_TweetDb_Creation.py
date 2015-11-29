# -*- coding: utf-8 -*-

# To run this code, first edit config.py with your configuration, then:
#
# python MongoDb_TweetDb_Creation.py -q apple
# 
# It will produce the list of tweets for the query "apple" 
# in the MongoDb Database @ c:\data\db\

import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import argparse
import string
import config
import json
from pymongo import MongoClient

def get_parser():
    """Get parser for command line arguments."""
    parser = argparse.ArgumentParser(description="Twitter Downloader")
    parser.add_argument("-q",
                        "--query",
                        dest="query",
                        help="Query/Filter",
                        default='-')
    return parser


class MyListener(StreamListener):
    """Custom StreamListener for streaming data."""

    def __init__(self, query):
        query_fname = format_filename(query)
        self.outfile = "stream_%s" % (query_fname)

    def on_data(self, data):
        try:
            client = MongoClient('localhost', 27017)
            db = client[self.outfile]
            collection = db[self.outfile + 'Collection']
            tweet = json.loads(data)
            collection.insert(tweet)   
            print tweet['text']
            return True
        except BaseException, e:
            print 'failed ondata,', str(e)
            time.sleep(1)
            pass
            

    def on_error(self, status):
        print(status)
        return True


def format_filename(fname):
    """Convert file name into a safe string.
    Arguments:
        fname -- the file name to convert
    Return:
        String -- converted file name
    """
    return ''.join(convert_valid(one_char) for one_char in fname)


def convert_valid(one_char):
    """Convert a character into '_' if invalid.
    Arguments:
        one_char -- the char to convert
    Return:
        Character -- converted char
    """
    valid_chars = "-_.%s%s" % (string.ascii_letters, string.digits)
    if one_char in valid_chars:
        return one_char
    else:
        return '_'

@classmethod
def parse(cls, api, raw):
    status = cls.first_parse(api, raw)
    setattr(status, 'json', json.dumps(raw))
    return status

if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()
    auth = OAuthHandler(config.consumer_key, config.consumer_secret)
    auth.set_access_token(config.access_token, config.access_secret)
    api = tweepy.API(auth)

    twitter_stream = Stream(auth, MyListener(args.query))
    twitter_stream.filter(track=[args.query])