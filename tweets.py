from twitter import *
import pandas as pd
from datetime import datetime as dt
import time
import glob
import os
import sys
import json
import simplejson
import pdb
import twitter

def oauth_login():
    # XXX: Go to http://twitter.com/apps/new to create an app and get values
    # for these credentials that you'll need to provide in place of these
    # empty string values that are defined as placeholders.
    # See https://dev.twitter.com/docs/auth/oauth for more information
    # on Twitter's OAuth implementation.

    CONSUMER_KEY = '3vhPtpq5VjXpz1SVh3z2nc1Gu'
    CONSUMER_SECRET = 'vW223v1O7537APiEsPq2U52oLsqtcZMEZzoSoHanBE6hIiQo9U'
    OAUTH_TOKEN = '941412073392701442-x7cBQoqEx8g81iRj2BlqQ5sIz9MNHbT'
    OAUTH_TOKEN_SECRET = 'NiWLPN8lfPa7GOGwbQ8TetlqWVp7JFf1XXHbuUoq0c1Tz'

    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

    twitter_api = twitter.Twitter(auth=auth)
    return twitter_api

def TwitterSearch(twitterApi, query, approxCount = 3000, **kw):
    searchResults = twitterApi.search.tweets(q= query, count=100, **kw)
    statuses = searchResults['statuses']
    while len(statuses) < approxCount:
        try:
            nextResults = searchResults['search_metadata']['next_results']
        except KeyError as e:
            break
        print( str(len(statuses)) + ' results have been downloaded from approximately ' + str(approxCount))
        kwargs = dict([ kv.split('=') for kv in nextResults[1:].split("&") ])
        nextResults = twitter_api.search.tweets(**kwargs)
        statuses += nextResults['statuses'] # cool append notation
        print( 'A total of ' + str(len(statuses)) + ' have been downloaded')
    return statuses

dir=(r'./')

twitter_api = oauth_login()

q = input("What would you like to search for(ex: BTC, ETH, XRP, IOTA)?\n")

statuses = TwitterSearch(twitter_api, q, approxCount = 2000)

json_dump = json.dumps(statuses)

# for _ in range(30):
	# print( "Length of statuses", len(statuses))
	# try:
		# next_statuses = search_statuses['search_metadata']['next_statuses']
	# except KeyError, e: # No more statuses when next_statuses doesn't exist
		# break

# kwargs = dict([ kv.split('=') for kv in next_statuses[1:].split("&") ])
# search_statuses = twitter_api.search.tweets(**kwargs)

status_id = [status['id'] for status in statuses]
name = [status['user']['name'] for status in statuses ]
screen_name = [status['user']['screen_name'] for status in statuses ]
status_text = [status['text'] for status in statuses ]
location = [status['user']['location'] for status in statuses ]
geo = [status['geo']for status in statuses ]
time_zone = [status['user']['time_zone']for status in statuses ]
friend_count =  [status['user']['friends_count'] for status in statuses]
follower_count = [status['user']['followers_count'] for status in statuses]
tmstamp = [status['created_at'] for status in statuses]
retweet_ct = [status['retweet_count'] for status in statuses]
source = [status['source'] for status in statuses]
place = [status['place'] for status in statuses]

data = {'status_id' : status_id,
        'name' : name,
        'screen_name' : screen_name,
        'status_text' : status_text,
        'tmstamp' : tmstamp,
        'time_zone' : time_zone,
        'location' : location,
        'geo' : geo,
        'friend_count' : friend_count,
        'follower_count' : follower_count,
        'retweet_count' : retweet_ct,
        'source' : source,
        'place' : place}

relevant_data = {
        'name' : name,
        'status_text' : status_text,
        'retweet_count' : retweet_ct,
        'follower_count' : follower_count,
        'tmstamp' : tmstamp
        }

df = pd.DataFrame(relevant_data)
fname = dir + q + str(dt.now().strftime("%Y-%m-%d_%H-%M-%S"))

yes_no = input("Would you like to save the output as a csv for storage? y/n \n")
if yes_no.lower() == "y" or "yes":
    with codecs.open(fname,'r','utf-8') as f:
        tweets = json.load(f, encoding='utf-8')
        print(tweets[2])
    df.to_csv('{}.csv'.format(fname), encoding = 'utf-8')
    with codecs.open(fname+'.json','r','utf-8') as f:
        f.write(json.dumps(json.loads(json_dump), indent=4, sort_keys=True))
        f.close()
    print("Saved as {}{} and {}{}".format(fname, '.csv', fname, '.json'))
else:
    "The file will not be saved."
