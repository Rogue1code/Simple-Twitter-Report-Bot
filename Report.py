#!/usr/bin/python2.7
#pip install tweepy
#fill out Secrets.py with your secrets
#Provide a list.txt and fill it with user id not usernames

print '_______________________________________________________'
print '|"""""""""""""""""""""""""""""""""""""""""""""""""""""|'
print '|"""""""""""""""""""""""""""""""""""""""""""""""""""""|'
print '|"_______"""""""""""""""""""""""""""""""""""""""""""""|'
print '||       \ """""""""""""""""""""""""""""""""""""""""""|'
print '|| $$$$$$$\  ______    ______   __    __   ______ """"|'
print '|| $$__| $$ /      \  /      \ |  \  |  \ /      \ """|'
print '|| $$    $$|  $$$$$$\|  $$$$$$\| $$  | $$|  $$$$$$\ ""|'
print '|| $$$$$$$\| $$  | $$| $$  | $$| $$  | $$| $$    $$ ""|'
print '|| $$  | $$| $$__/ $$| $$__| $$| $$__/ $$| $$$$$$$$ ""|'
print '|| $$  | $$ \$$    $$ \$$    $$ \$$    $$ \$$     \ ""|'
print '| \$$   \$$  \$$$$$$  _\$$$$$$$  \$$$$$$   \$$$$$$$ ""|'
print '|""""""""""""""""""""|  \__| $$"""""""""""""""""""""""|'
print '|"""""""""""""""""""""\$$    $$"""""""""""""""""""""""|'
print '|""""""""""""""""""""""\$$$$$$""""""""""""""""""""""""|'
print '|"""""""""""""""""""""""""""""""""""""""""""""""""""""|'
print '|"""""""""""""Simple Twitter User Grabber"""""""""""""|'
print '|"""""""""""""""""""""""""""""""""""""""""""""""""""""|'
print '|_____________________________________________________|'

#_______________________________________________________________

import tweepy,time,sys,csv,os
import argparse
from urlparse import urlparse

__version__ = '0.1'

try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse


from secrets import consumer_key, consumer_secret, access_token, access_token_secret


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)



f=open("list.txt", "r,w")
for line in f.readlines():
    user = line
    print "now Reporting", (user)
    api.report_spam(user)
    api.create_block(user)
f.close()
