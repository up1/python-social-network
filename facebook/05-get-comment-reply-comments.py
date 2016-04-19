import requests
import pprint
import arrow

api_url = "https://graph.facebook.com/v2.5"
comment_id = "507821849424156_507822546090753"
endpoint = "%s/%s/comments" % (api_url, comment_id)

access_token = "xxxxxx"
payload = {
        'access_token': access_token,
        'fields': ','.join(['id', 'created_time', 'message', 'from']),
        'limit': 50
        }

response = requests.get(endpoint, params=payload).json()
for comment in response['data']:
    print comment['id']
    print comment['created_time']

print len(response['data'])
