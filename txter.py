from bandwidth_sdk import Message
from bandwidth_sdk import Client
# import requests
from mylogins import user, token, secret, orig
Client(user, token, secret)

class Txter:
    def send(self,message,orig):
        Message.send(
          sender=orig,
          receiver='+17206925355',
          text=message,
          tag='test tag')

txt = Txter('this is messge', '+17206925355')
# Message('m-id123213', state='sending')

#url = 'http://ip-api.com/json'

#response = requests.get(url)

#print response.text
# install sdk: pip install bandwidth_sdk
