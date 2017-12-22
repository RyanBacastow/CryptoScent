import requests
import json
import boto3
##call coin info from cryptocompare.com
coin_response = requests.get('https://min-api.cryptocompare.com/data/all/coinlist')
coinlist_json = coin_response.json()
coinlist = coinlist_json['Data']
## The below function created the table, it will not work if ran again as
##the table already exists
dynamodb = boto3.resource('dynamodb')
table = dynamodb.create_table(
    TableName='Coin_List',
    KeySchema=[{'AttributeName': 'Symbol',\
    'KeyType': 'HASH'},{'AttributeName': 'CoinName','KeyType': 'RANGE'}],\
    AttributeDefinitions=[{'AttributeName': 'Symbol',\
    'AttributeType': 'S'},{'AttributeName': 'CoinName','AttributeType': 'S'},],\
    ProvisionedThroughput={'ReadCapacityUnits': 40,'WriteCapacityUnits': 40})
table.meta.client.get_waiter('table_exists').wait(TableName='Coin_List')
##batch load info from cryptocompare to Coin_List table
table = dynamodb.Table('Coin_List')
for key in coinlist:
    with table.batch_writer() as batch:
        batch.put_item(Item=coinlist[key])
