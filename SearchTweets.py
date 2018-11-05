# code by Rajshree
from Utils import oauth_req

# building the query string from the post form data


def buildquerydataforsearch(formdata):
    querydata = '?'

    if formdata['parameters_q'] != "":
        querydata = querydata + 'q=' + formdata['parameters_q']
    if formdata['parameters_geocode'] != "":
        querydata = querydata + '&geocode=' + formdata['parameters_geocode']
    if formdata['parameters_lang'] != "":
        querydata = querydata + '&lang=' + formdata['parameters_lang']
    if formdata['parameters_locale'] != "":
        querydata = querydata + '&locale=' + formdata['parameters_locale']
    if formdata['parameters_result_type'] != "":
        querydata = querydata + '&result_type=' + formdata['parameters_result_type']
    if formdata['parameters_count'] != "":
        querydata = querydata + '&count=' + formdata['parameters_count']
    if formdata['parameters_until'] != "":
        querydata = querydata + '&until=' + formdata['parameters_until']
    if formdata['parameters_since_id'] != "":
        querydata = querydata + '&since_id=' + formdata['parameters_since_id']
    if formdata['parameters_max_id'] != "":
        querydata = querydata + '&max_id=' + formdata['parameters_max_id']
    if formdata['parameters_include_entities'] != "":
        querydata = querydata + '&include_entities=' + formdata['parameters_include_entities']
    return oauth_req('https://api.twitter.com/1.1/search/tweets.json' + querydata)
