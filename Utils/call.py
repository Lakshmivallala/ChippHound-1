from twilio.rest import Client
import os


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = "AC0c484b63bf25368d26340361b0c61aa8"
auth_token = "2d7e7d1d61d3bee25672b8ac608c500f"
client = Client(account_sid, auth_token)

call = client.calls.create(
                        url='http://demo.twilio.com/docs/classic.mp3',
                        to='+917987523794',
                        from_='+12057083227'
                    )

print(call.sid)
# http://demo.twilio.com/docs/classic.mp3
# https://www.dropbox.com/s/it66o7aj75uogzz/audiooooo.mp3?dl=0