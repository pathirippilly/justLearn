from twilio.rest import Client
client = Client("AC5d10e596a1a9cc93bffd20e16f568b1f","8e5a4927c07a2f1c79cc359344025af8")

msg=client.messages.create(
    to="+919745060076",
    from_="+12064663448",
    body="from pycharm")

print(f"{msg.from_} sent a new message created by {msg.account_sid}")

list