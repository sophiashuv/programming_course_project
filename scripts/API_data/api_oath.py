import http.client

conn = http.client.HTTPSConnection("api.dexcom.com")

payload = "client_secret=RQ8fXSagHmCLPp4B&client_id=a0mtnbPsKowXj4qRC3XRhoEpCJrWzXtO&code=83151223d8d0260af8f9e219b43f7e70&grant_type=authorization_code&redirect_uri=https://twitter.com/"

headers = {
    'content-type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache"
    }

conn.request("POST", "/v2/oauth2/token", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
