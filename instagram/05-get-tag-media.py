import requests
import pprint
import arrow

api_url = "https://api.instagram.com/v1"
tag_name = "hello"
endpoint = "%s/tags/%s/media/recent" % (api_url, tag_name)

client_id = "xxxxxx"
payload = { 'client_id': client_id, 'count': 30 }

response = requests.get(endpoint, params=payload).json()
for media in response['data']:
    print media['id']
    print arrow.get(media['created_time'])

print "\nPost count: %d\n" % len(response['data'])
