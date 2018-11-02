# code by Rajshree
from Utils import oauth_req

# building the query string from the post form data


def buildquerydataforusertimeline(formdata):
    querydata = '?'

    if formdata['parameters_user_id'] != "":
        querydata = querydata + 'user_id=' + formdata['parameters_user_id']
    if formdata['parameters_screen_name'] != "":
        querydata = querydata + '&screen_name=' + formdata['parameters_screen_name']
    if formdata['parameters_since_id'] != "":
        querydata = querydata + '&since_id=' + formdata['parameters_since_id']
    if formdata['parameters_count'] != "":
        querydata = querydata + '&count=' + formdata['parameters_count']
    if formdata['parameters_max_id'] != "":
        querydata = querydata + '&max_id=' + formdata['parameters_max_id']
    return oauth_req('https://api.twitter.com/1.1/statuses/user_timeline.json' + querydata)
