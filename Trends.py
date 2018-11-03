from Utils import oauth_req


def buildtrendsquery(formdata):
    querydata = '?'

    if formdata['parameters_id'] != "":
        querydata = querydata + 'id=' + formdata['parameters_id']
    if formdata['parameters_exclude'] != "":
        querydata = querydata + 'exclude' + formdata['parameters_exclude']

    return oauth_req('https://api.twitter.com/1.1/trends/place.json' + querydata)


