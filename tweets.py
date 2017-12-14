import os
import codecs
import json
from twitterscraper import query_tweets
from twitterscraper.query import query_all_tweets
import pandas as pd
import numpy as np

df = pd.DataFrame()

def main():
    keyword = input("What words would you like to search for?\n")
    number = int(input("How many tweets would you like me to filter through?\n"))
    fname = input("Name your output file.\n")
    fname = fname + '.json'
    query = 'twitterscraper {} -l {} -o {}'.format(keyword, number,fname)
    os.system(query)
    with codecs.open(fname,'r','utf-8') as f:
        tweets = json.load(f, encoding='utf-8')
        for tweet in tweets:
            if int(tweet['likes'])> 1 or int(tweet['retweets']) > 1:
                print(tweet['text'],'\n')
        df.append([tweet['text']])
        
if __name__ == '__main__':
    main()
