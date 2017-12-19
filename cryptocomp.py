import requests
import json
import pandas as pd
import numpy as np

coin_response = requests.get('https://min-api.cryptocompare.com/data/all/coinlist')
coinlist_json = coin_response.json()
global coinlist
coinlist= pd.DataFrame(coinlist_json['Data'])
coinlist = coinlist.transpose()
vol_price = {}
concating_frames = []
for coin in coinlist['Name']:
    try:
        
        params = {'fsym': coin, 'tsym':'USD', 'limit': 2000}
        print(coin)
        response = requests.get('https://min-api.cryptocompare.com/data/histoday', params=params)
        data = response.json()
        hist_df = pd.DataFrame(data['Data'])
        hist_df['Average Price']=hist_df[['open','close','high','low']].mean(axis=1)
        hist_df['Average Volume'] = hist_df[['volumefrom', 'volumeto']].mean(axis=1)
        vol_price[coin]=hist_df['Average Price'].corr(hist_df['Average Volume'])
        hist_df = hist_df.rename(columns={'open':coin+'_open','close':coin+'_close',\
                                                      'high':coin+'_high','low':coin+'_low',\
                                                      'volumefrom':coin+'_volumefrom',\
                                                      'volumeto':coin+'_volumeto',\
                                                      'Average Price':coin+'_Average Price',\
                                                      'Average Volume':coin+'_Average Volume'})
        
        concating_frames.append(hist_df)
    except KeyError:
        continue
coinlist['Volume to Price Corr'] = coinlist['Name'].map(vol_price)
master_hist_df = pd.concat(concating_frames, axis=1)
correlation_concate = []
for ticker in coinlist['Name']:
    try:
        correlation_concate.append(master_hist_df[ticker+'_Average Price'])
    except KeyError:
        continue
corr_matrix_df = pd.concat(correlation_concate, axis=1)
corr_matrix_df = corr_matrix_df.pct_change().corr(method='pearson')
coinlist.to_csv('coinlist.csv', encoding='utf-8', index=False)
master_hist_df.to_csv('master_hist_df.csv', encoding='utf-8', index=False)
corr_matrix_df.to_csv('corr_matrix.csv', encoding='utf-8', index=False)


    


