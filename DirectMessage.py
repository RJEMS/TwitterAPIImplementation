# code by Matt
import Utils

# building the query string from the post form data


def buildquerydatafordirectmessage(formdata):
    querydata = '?'

    if formdata['parameters_since_id'] != "":
        querydata = querydata + 'since_id=' + formdata['parameters_since_id']
    if formdata['parameters_max_id'] != "":
        querydata = querydata + '&max_id=' + formdata['parameters_max_id']
    if formdata['parameters_count'] != "":
        querydata = querydata + '&count=' + formdata['parameters_count']
    return Utils.oauth_req('https://api.twitter.com/1.1/direct_messages.json' + querydata)
