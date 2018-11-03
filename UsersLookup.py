# code by Emmeline
from Utils import oauth_req


# building the query string from the post form data


def buildlookup(formdata):
    querydata = '?'

    if formdata['parameters_screen_name'] != "":
        querydata = querydata + '&screen_name=' + formdata['parameters_screen_name']
    if formdata['parameters_user_id'] != "":
        querydata = querydata + '&user_id=' + formdata['parameters_user_id']
    if formdata['parameters_include_entities'] != "":
        querydata = querydata + '&include_entities=' + formdata['parameters_include_entities']

    print (querydata)
    return oauth_req('https://api.twitter.com/1.1/users/lookup.json' + querydata)
