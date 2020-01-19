from twilio.rest import Client
import os


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = "AC4cbc274e4b13e29097e628e4e98afbc9"
auth_token = "cbed0cb6d1a66f290f7d2c5820324009"
client = Client(account_sid, auth_token)

call = client.calls.create(
                        url='http://demo.twilio.com/docs/classic.mp3',
                        to='+917987523794',
                        from_='+12057083227'
                    )

print(call.sid)
# http://demo.twilio.com/docs/classic.mp3
# https://www.dropbox.com/s/it66o7aj75uogzz/audiooooo.mp3?dl=0