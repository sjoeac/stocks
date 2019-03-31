from nsetools import Nse
from prometheus_client import Gauge,CollectorRegistry,pushadd_to_gateway
import requests
import sys
import datetime
import os


d = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")

nse = Nse()

stock_list = [
{
    "symbol" : 'VAKRANGEE',
},
{
    "symbol" : 'IOC',
},
]

def my_function(price,symbol):
  registry = CollectorRegistry()
  last_success = Gauge('price', 
      'Unixtime stock job last succeeded', registry=registry)
  last_success.set(price)
  pushadd_to_gateway('localhost:9091', job=symbol, registry=registry)




for stock in stock_list:
    stats = nse.get_quote(stock['symbol'])
    print stock['symbol']
    print stats['dayHigh']

    price = stats['dayHigh']
    symbol = stock['symbol']
    my_function(price,symbol)
