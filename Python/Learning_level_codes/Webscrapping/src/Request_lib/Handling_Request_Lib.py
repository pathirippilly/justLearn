import http.client
conn = http.client.HTTPSConnection("api.twilio.com")
payload = 'Body=Post%20man%20message&From=+12064663448&To=+919745060076&MediaUrl=https%3A//media.giphy.com/media/FgiHOQyKUJmwg/giphy.gif'
headers = {
  'Authorization': 'Basic QUM1ZDEwZTU5NmExYTljYzkzYmZmZDIwZTE2ZjU2OGIxZjo4ZTVhNDkyN2MwN2EyZjFjNzljYzM1OTM0NDAyNWFmOA==',
  'Content-Type': 'application/x-www-form-urlencoded'
}
conn.request("POST", "/2010-04-01/Accounts/AC5d10e596a1a9cc93bffd20e16f568b1f/Messages.json", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))