import requests
import json
import os
import pandas as pd
import numpy as np

coin_response = requests.get('https://min-api.cryptocompare.com/data/all/coinlist')
coinlist_json = coin_response.json()
global coinlist
coinlist= pd.DataFrame(coinlist_json['Data'])
coinlist = coinlist.transpose()
print('coin list generated')
global master_hist_df
master_hist_df = pd.DataFrame()
def coin_correlation(df):
    try:
        params = {'fsym':df['Name'], 'tsym':'USD', 'limit': 2000}
        print('sent ' + df['Name'])
        hist_price_response = requests.get('https://min-api.cryptocompare.com/data/histoday', params=params)
        hist_price = hist_price_response.json()
        hist_price_df = pd.DataFrame(hist_price['Data'])
        hist_price_df['Average Price'] = hist_price_df[['open','close','high','low']].mean(axis=1)
        hist_price_df['Average Volume'] = hist_price_df[['volumefrom', 'volumeto']].mean(axis=1)
        hist_price_df = hist_price_df.rename(columns={'open':df['Name']+'_open','close':df['Name']+'_close',\
                                                      'high':df['Name']+'_high','low':df['Name']+'_low',\
                                                      'volumefrom':df['Name']+'_volumefrom',\
                                                      'volumeto':df['Name']+'_volumeto',\
                                                      'Average Price':df['Name']+'_Average Price',\
                                                      'Average Volume':df['Name']+'_Average Volume'})
        master_hist_df = pd.concat([master_hist_df ,hist_price_df],axis=1)             
        return hist_price_df['Average Price'].corr(hist_price_df['Average Volume'])
    except KeyError:
        return 'NA'
coinlist['Volume to Price Correlation'] = coinlist.apply(coin_correlation, axis = 1)
coinlist.to_csv('coinlist.csv', encoding='utf-8', index=False)
master_hist_df.to_csv('master_hist_df.csv', encoding='utf-8', index=False)
corr_matrix_df = pd.DataFrame()
for ticker in coinlist['Symbol']:
    corr_matrix_df = pd.concat([corr_matrix_df, master_hist_df[ticker+'_Average Price']],axis=1)
corr_matrix_df.pct_change().corr(method='pearson')
corr_matrix_df.to_csv('corr_matrix.csv', encoding='utf-8', index=False)

    


