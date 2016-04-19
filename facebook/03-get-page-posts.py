import requests
import pprint
import arrow

api_url = "https://graph.facebook.com/v2.5"
page_id = "421936097949882"
endpoint = "%s/%s/feed" % (api_url, page_id)

access_token = "xxxxxx"
payload = {
        'access_token': access_token,
        'fields': ','.join(['id', 'created_time', 'updated_time', 'message', 'from', 'permalink_url', 'type', 'shares']),
        'limit': 50
        }

response = requests.get(endpoint, params=payload).json()
for post in response['data']:
    print post['id']
    print post['created_time']

print len(response['data'])

# specific time
payload['since'] = arrow.get(2015, 1, 1).timestamp
payload['until'] = arrow.get(2015, 1, 3).timestamp
response = requests.get(endpoint, params=payload).json()
for post in response['data']:
    print post['id']
    print post['created_time']
