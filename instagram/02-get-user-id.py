# https://www.instagram.com/aum_patchrapa/

import requests
import pprint

api_url = "https://api.instagram.com/v1"
endpoint = "%s/users/search" % api_url

username = "aum_patchrapa"
client_id = "xxxxxx"
payload = { 'q': username, 'client_id': client_id }

for user in requests.get(endpoint, params=payload).json()['data']:
    if user['username'] == username:
        print user['id']
