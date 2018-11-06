# code by Jonathan
from Utils import oauth_post
from urllib.parse import quote

# building the query string from the post form data


def builddeletetweet(formdata):
    querydata = 'https://api.twitter.com/1.1/statuses/destroy/'

    if formdata['parameters_id'] != "":
        querydata = querydata + quote(formdata['parameters_id']) + '.json'
    return oauth_post(querydata)
