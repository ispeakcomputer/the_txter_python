import requests

#url = 'http://ip-api.com/json'

#response = requests.get(url)

#print response.text
# install sdk: pip install bandwidth_sdk

from bandwidth_sdk import Message
from bandwidth_sdk import Client

user = ''
token = 't-7vtwydiyqmn3lis67dh6hvq'
secret = ''

print user
print token
print secret

Client(user, token, secret)

Message.send(
    sender='+',
    receiver='+17206925355',
    text='Host is approching critical condition: Reason - LOAD > 90%',
    tag='test tag')
# Message('m-id123213', state='sending')
