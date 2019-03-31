from pprint import pprint # just for neatness of display
from nsetools import Nse
import requests

released = [
{
    "stock" : 'IDEA',
    "lthreshold" : 80,
    "uthreshold" : 100
},

{
    "stock" : 'PFC',
    "lthreshold" : 100,
    "uthreshold" : 140
},

{
    "stock" : 'PNB',
    "lthreshold" : 100,
    "uthreshold" : 145
},

{
    "stock" : 'HCC',
    "lthreshold" : 25,
    "uthreshold" : 45
},
{
    "stock" : 'ADANIPOWER',
    "lthreshold" : 35,
    "uthreshold" : 45
},
{
    "stock" : 'SUZLON',
    "lthreshold" : 15,
    "uthreshold" : 35
},
{
    "stock" : 'SINTEX',
    "lthreshold" : 25,
    "uthreshold" : 35
},

{
    "stock" : 'GRANULES',
    "lthreshold" : 120,
    "uthreshold" : 130
},
{
    "stock" : 'HDIL',
    "lthreshold" : 35,
    "uthreshold" : 45
},
{
    "stock" : 'RNAVAL',
    "lthreshold" : 25,
    "uthreshold" : 35
},
{
    "stock" : 'RCOM',
    "lthreshold" : 25,
    "uthreshold" : 35
}



]

#Email paramaters
sender_email = '@gmail.com'
sender_name = 'Stephen'
content = ''

nse = Nse()
for color in released:
    q = nse.get_quote(color['stock'])
    print(q)
    #if q['open'] < color['lthreshold']:
    if q['open'] > color['lthreshold'] and  q['open'] < color['uthreshold']:
        content += color['stock'] + ":" + str(q['open'])


url = "https://api.sendgrid.com/v3/mail/send"

payload = '{"personalizations":[{"to":[{"email":"s@gmail.com","name":"Stephen"}],"subject":"Hello, World!"}],"from":{"email":"s@gmail.com","name":"Sam Smith"},"reply_to":{"email":"s@gmail.com","name":"Sam Smith"},"subject":"Hello, World!","content":[{"type":"text/html","value":"test"}]}'

payload = '{"personalizations":[{"to":[{"email":"' + sender_email + '","name":"'+ sender_name +'"}],"subject":"Stock Alert!"}],"from":{"email":"' + sender_email + '","name":"' + sender_name + '"},"reply_to":{"email":"' + sender_email + '","name":"' + sender_name + '"},"subject":"Stock Alert!","content":[{"type":"text/html","value":"' + content + '"}]}'

headers = {
    'authorization': "",
    'content-type': "application/json"
    }

if content:
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)


