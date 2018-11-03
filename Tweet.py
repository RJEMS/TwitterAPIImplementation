# code by Jonathan
from Utils import oauth_post
from urllib.parse import quote

# building the query string from the post form data


def buildtweet(formdata):
    querydata = '?'

    if formdata['parameters_tweet'] != "":
        querydata = querydata + 'status=' + quote(formdata['parameters_tweet'])
    return oauth_post('https://api.twitter.com/1.1/statuses/update.json' + querydata)
