# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


account_sid = 'ACb1de48523a750d6444d12bf9b07ac9aa'
auth_token = '574056611b247caa0015348da6593459'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Violence Detected near NIT Raipur!",
                     from_='+18146867354',
                     to='+9170917 00838'
                 )

print(message.sid)
