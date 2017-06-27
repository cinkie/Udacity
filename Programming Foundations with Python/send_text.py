from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC47555409d6116688fb6c5e61b9e07e90"
# Your Auth Token from twilio.com/console
auth_token  = "00cff81daa45c913fd63a61c5d4d8754"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+15129706630", 
    from_="+15129007002",
    body="Hello from Python")

print(message.sid)
