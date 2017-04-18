#!/usr/bin/python

from bandwidth_sdk import Client
from mylogins import user, token, secret, orig
from bandwidth_sdk import Message

print "  user     " + user + "  token    " + token + "  secret    " + secret

Client(user, token, secret)

Message.send(
    sender='+17204647640',
    receiver='+17206925355',
    text='Alert - Motion Detected',
    tag='test tag')

    # def checklen(ourmessage):
    #     if len(ourmessage) >= 140:
    #
