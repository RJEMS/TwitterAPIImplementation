# Code by Emmeline
from Utils import oauth_req, oauth_post
import json, warnings, unittest, string, random


# Disabling warning messages when running unit test
def ignore_warnings(test_func):
    def do_test(self, *args, **kwargs):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", 'ResourceWarning')
            test_func(self, *args, **kwargs)
    return do_test



# Unit tests for oauth_req and oauth_post methods
class Testing(unittest.TestCase):

    # Test valid GET request using oauth_req
    @ignore_warnings
    def test_valid_oauthreq(self):
        url = 'https://api.twitter.com/1.1/users/lookup.json?&screen_name=realDonaldTrump'
        res = oauth_req(url)
        json_data = json.loads(res)

        # verify json object is returned from request
        assert 'id' in json_data[0]
        assert 'name' in json_data[0]

        # verify there's no error code from request
        assert 'code' not in json_data[0]

    # Test invalid GET request using oauth_req
    @ignore_warnings
    def test_invalid_oauthreq(self):
        url = 'https://api.twitter.com/1.1/search/tweets.json'
        res = oauth_req(url)
        json_data = json.loads(res)

        # verify API is missing required query paramters
        assert json_data['errors'][0]['message'] == 'Query parameters are missing.'


    # Test valid POST request using oauth_post
    @ignore_warnings
    def test_valid_oauthpost(self):
        # Generate random string to update status
        chars = string.ascii_uppercase
        random_chars = ''.join(random.choice(chars) for _ in range(10))
        url = 'https://api.twitter.com/1.1/statuses/update.json?status=' + random_chars
        res = oauth_post(url)
        json_data = json.loads(res)

        # verify the status is in the response
        assert json_data['text'] == random_chars


    # Test invalid POST request using oauth_post
    @ignore_warnings
    def test_invalid_oauthpost(self):
        # Generate random string to update status
        chars = string.ascii_uppercase
        random_chars = ''.join(random.choice(chars) for _ in range(10))
        url = 'https://api.twitter.com/1.1/statuses/update.json'
        res = oauth_post(url)
        json_data = json.loads(res)

        # verify the error message, status parameter is missing
        assert json_data['errors'][0]['message'] == 'Missing required parameter: status.'



if __name__ == '__main__':
    unittest.main()
