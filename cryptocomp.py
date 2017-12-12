import requests
import json
import pandas as pd
import numpy as np

coin_response = requests.get('https://min-api.cryptocompare.com/data/all/coinlist')
coinlist_json = coin_response.json()
coinlist= pd.DataFrame(coinlist_json['Data'])
coinlist = coinlist.transpose()
#def coin_correlation(df):
#    try:
#        params = {'fsym':df['Name'], 'tsym':'USD', 'limit': 2000}
#        print('sent' + df['Name'])
#        hist_price_response = requests.get('https://min-api.cryptocompare.com/data/histoday', params=params)
#        hist_price = hist_price_response.json()
#        hist_price_df = pd.DataFrame(hist_price['Data'])
#        hist_price_df['Average Price'] = hist_price_df[['open','close','high','low']].mean(axis=1)
#        hist_price_df['Average Volume'] = hist_price_df[['volumefrom', 'volumeto']].mean(axis=1)
#        return hist_price_df['Average Price'].corr(hist_price_df['Average Volume'])
#    except KeyError:
#        return 'NA'
#coinlist['Volume to Price Correlation'] = coinlist.apply(coin_correlation, axis = 1)
#print(coinlist.head())
data_1 = coinlist[:501]
data_2 = coinlist[500:1000]
print(data_1.tail(1))
print(data_2.head(1))

