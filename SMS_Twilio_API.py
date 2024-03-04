from twilio.rest import Client

account_sid = 'AC556c0fe8735dc8042185481deb46058f'
auth_token = '[AuthToken]'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from='+18442532975',
  body='Thanks Twilio for the MSN',
  to='+14704031009'
)

print(message.sid)