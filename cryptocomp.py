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
master_hist_df = pd.DataFrame()
#def coin_correlation(df):
#    try:
#        params = {'fsym':df['Name'], 'tsym':'USD', 'limit': 2000}
#        print('sent' + df['Name'])
#        hist_price_response = requests.get('https://min-api.cryptocompare.com/data/histoday', params=params)
#        hist_price = hist_price_response.json()
#        hist_price_df = pd.DataFrame(hist_price['Data'])
#        hist_price_df['Average Price'] = hist_price_df[['open','close','high','low']].mean(axis=1)
#        hist_price_df['Average Volume'] = hist_price_df[['volumefrom', 'volumeto']].mean(axis=1)
#        hist_price_df = hist_price_df.rename(columns={'open':df['Name']+'_open','close':df['Name']+'_close',\
#                                                      'high':df['Name']+'_high','low':df['Name']+'_low',\
#                                                      'volumefrom':df['Name']+'_volumefrom',\
#                                                      'volumeto':df['Name']+'_volumeto',\
#                                                      'Average Price':df['Name']+'_Average Price',\
#                                                      'Average Volume':df['Name']+'_Average Volume'})
#        master_hist_df = master_hist_df.append(hist_price_df)               
#        return hist_price_df['Average Price'].corr(hist_price_df['Average Volume'])
#    except KeyError:
#        return 'NA'
#coinlist['Volume to Price Correlation'] = coinlist.apply(coin_correlation, axis = 1)
#print(coinlist.head())
print('starting test')
params = {'fsym':'BTC', 'tsym':'USD', 'limit': 2000}
btc_price_response = requests.get('https://min-api.cryptocompare.com/data/histoday', params=params)
btc_price = btc_price_response.json()
btc_price_df = pd.DataFrame(btc_price['Data'])
btc_price_df['Average Price'] = btc_price_df[['open','close','high','low']].mean(axis=1)
name = 'BTC'
##Eureka! Create empty dataframe, append each new DF with name of ticker as below
btc_price_df = btc_price_df.rename(columns={"open":name+"_open",'close':name+'_close','high':name+'_high',\
                                            'low':name+'_low','volumefrom':name+'_volumefrom','volumeto':name+'_volumeto',\
                                            'Average Price':name+'_Average Price','time':name+'_time'})
master_hist_df = pd.concat([master_hist_df,btc_price_df], ignore_index=True,axis =1)
#print(master_hist_df.describe())
params = {'fsym':'LTC', 'tsym':'USD', 'limit': 2000}
ltc_price_response = requests.get('https://min-api.cryptocompare.com/data/histoday', params=params)
ltc_price = ltc_price_response.json()
ltc_price_df = pd.DataFrame(ltc_price['Data'])
ltc_price_df['Average Price'] = ltc_price_df[['open','close','high','low']].mean(axis=1)
namel = 'LTC'
ltc_price_df = ltc_price_df.rename(columns={"open":namel+"_open",'close':namel+'_close','high':namel+'_high',\
                                            'low':namel+'_low','volumefrom':namel+'_volumefrom','volumeto':namel+'_volumeto',\
                                            'Average Price':namel+'_Average Price','time':namel+'_time'})
master_hist_df = pd.concat([master_hist_df ,ltc_price_df], ignore_index=True,axis=1)
print(master_hist_df.head())
#master_hist_df = master_hist_df.append(ltc_price_df, ignore_index=True)
#print(master_hist_df.head())
#params = {'fsym':'ETH', 'tsym':'USD', 'limit': 2000}
#eth_price_response = requests.get('https://min-api.cryptocompare.com/data/histoday', params=params)
#eth_price = eth_price_response.json()
#eth_price_df = pd.DataFrame(eth_price['Data'])
#eth_price_df['Average Price'] = eth_price_df[['open','close','high','low']].mean(axis=1)


#print(ltc_price_df['Average Price'].corr(btc_price_df['Average Price']))

