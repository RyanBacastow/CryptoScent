import requests
import json

##https://www.reddit.com/dev/api API endpoints and params
params = {'t':'day'}
response_crypto = requests.get('http://www.reddit.com/r/CryptoCurrency/top/.json',\
                               params=params)
response_trading = requests.get('http://www.reddit.com/r/CryptoCurrencyTrading/top/.json',\
                               params=params)
crypto_data = response_crypto.json()
print(read)           
