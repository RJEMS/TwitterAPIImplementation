import oauth2

CLIENT_KEY = 'BcPXZRwvvcWCCMKU0tZsN2EGY'
CLIENT_SECRET = 'QwGSx6nFRYigJsszAGpZemDcgls1kp4otA3mEmsczwVi7u5y5J'


def oauth_req(url, key, secret, http_method="GET", post_body=b'', http_headers=None):
    consumer = oauth2.Consumer(key=CLIENT_KEY, secret=CLIENT_SECRET)
    token = oauth2.Token(key=key, secret=secret)
    client = oauth2.Client(consumer, token)
    resp, content = client.request(url, method=http_method, body=post_body, headers=http_headers)
    return content


home_timeline = oauth_req('https://api.twitter.com/1.1/statuses/user_timeline.json', '1050660458254876672-xos6g6ejyVBVvOJVg88VarkIQ8PqF9', '2EPXVunPLsG6CQBBMBXh6AbTpmdC9LWr5MjDIaga2N0xz')



print(home_timeline)



