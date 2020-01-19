from twilio.rest import Client
import os


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = "ACb1de48523a750d6444d12bf9b07ac9aa"
auth_token = "574056611b247caa0015348da6593459"
client = Client(account_sid, auth_token)

call = client.calls.create(
                        url='http://demo.twilio.com/docs/classic.mp3',
                        to='+917091700838',
                        from_='+18146867354'
                    )

print(call.sid)
# http://demo.twilio.com/docs/classic.mp3
# https://www.dropbox.com/s/it66o7aj75uogzz/audiooooo.mp3?dl=0