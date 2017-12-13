import requests
import json
import pandas as pd
import numpy as np

coin_response = requests.get('https://min-api.cryptocompare.com/data/all/coinlist')
coinlist_json = coin_response.json()
global coinlist
coinlist= pd.DataFrame(coinlist_json['Data'])
coinlist = coinlist.transpose()
print('coin list generated')
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
##print(coinlist.head())
print('starting test')
params = {'fsym':'BTC', 'tsym':'USD', 'limit': 2000}
btc_price_response = requests.get('https://min-api.cryptocompare.com/data/histoday', params=params)
btc_price = btc_price_response.json()
btc_price_df = pd.DataFrame(btc_price['Data'])
btc_price_df['Average Price'] = btc_price_df[['open','close','high','low']].mean(axis=1)
name = 'BTC'
##Eureka! Create empty dataframe, append each new DF with name of ticker as below
btc_price_df = btc_price_df.rename(columns={"open":name+"_open"})
print(btc_price_df.head())
#params = {'fsym':'LTC', 'tsym':'USD', 'limit': 2000}
#ltc_price_response = requests.get('https://min-api.cryptocompare.com/data/histoday', params=params)
#ltc_price = ltc_price_response.json()
#ltc_price_df = pd.DataFrame(ltc_price['Data'])
#ltc_price_df['Average Price'] = ltc_price_df[['open','close','high','low']].mean(axis=1)

#params = {'fsym':'ETH', 'tsym':'USD', 'limit': 2000}
#eth_price_response = requests.get('https://min-api.cryptocompare.com/data/histoday', params=params)
#eth_price = eth_price_response.json()
#eth_price_df = pd.DataFrame(eth_price['Data'])
#eth_price_df['Average Price'] = eth_price_df[['open','close','high','low']].mean(axis=1)


#print(ltc_price_df['Average Price'].corr(btc_price_df['Average Price']))

