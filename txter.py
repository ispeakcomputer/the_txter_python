#!/usr/bin/python
import bandwidth_sdk
from bandwidth_sdk import Client
from mylogins import user, token, secret, orig
from bandwidth_sdk import Message

# init a client to get started with the api
Client(user, token, secret)
print "Below you will see your api creds with you are loading your mylogin.py file correctly"
print "  user     " + user + "  token    " + token + "  secret    " + secret

class Txtbox:

    def sender(self, message, term):

        Message.send(
          sender='+17204647640',
          receiver=term,
          text=message,
          tag='test tag')

        return "Message sent successfully"

txtthing = Txtbox()
