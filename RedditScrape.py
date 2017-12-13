import requests
import json

params = {'t':'hour'}
response = requests.get('http://www.reddit.com/r/CryptoCurrency/top/.json', params=params)
read = response.json()
print(read)           
