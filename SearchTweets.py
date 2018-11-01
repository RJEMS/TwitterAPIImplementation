import requests
import base64
import pdb
from urllib.parse import parse_qs


def searchresults(formdata):
    searchparams = parse_qs(formdata['param'])

    print('122343', searchparams.get("parameters_q"))

    client_key = 'BcPXZRwvvcWCCMKU0tZsN2EGY'
    client_secret = 'QwGSx6nFRYigJsszAGpZemDcgls1kp4otA3mEmsczwVi7u5y5J'

    key_secret = '{}:{}'.format(client_key, client_secret).encode('ascii')
    b64_encoded_key = base64.b64encode(key_secret)
    b64_encoded_key = b64_encoded_key.decode('ascii')

    base_url = 'https://api.twitter.com/'
    auth_url = '{}oauth2/token'.format(base_url)

    auth_headers = {
        'Authorization': 'Basic {}'.format(b64_encoded_key),
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
    }

    auth_data = {
        'grant_type': 'client_credentials'
    }

    auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)

    access_token = auth_resp.json()['access_token']

    search_headers = {
        'Authorization': 'Bearer {}'.format(access_token)
    }

    search_params = {
        'q': 'music',
        'result_type': 'recent',
        'count': 1
    }

    search_url = '{}1.1/search/tweets.json'.format(base_url)

    search_resp = requests.get(search_url, headers=search_headers, params=search_params)
    search_data = search_resp.json()
    print(search_data)
    return search_data



