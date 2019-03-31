from pprint import pprint # just for neatness of display
from nsetools import Nse
from pprint import pprint 
import requests

released = [
{
    "stock" : 'VAKRANGEE',
    "lthreshold" : 80,
    "uthreshold" : 100
},

{
    "stock" : 'JIYAECO',
    "lthreshold" : 100,
    "uthreshold" : 140
},
]

nse = Nse()


for color2 in released:
    color = nse.get_quote("VAKRANGEE")
    pprint(color)


pprint(nse.get_stock_codes())

