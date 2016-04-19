import requests
import pprint
import arrow

api_url = "https://api.instagram.com/v1"
user_id = "9595407"
endpoint = "%s/users/%s/media/recent" % (api_url, user_id)

client_id = "xxxxxx"
payload = { 'client_id': client_id, 'count': 30 }

response = requests.get(endpoint, params=payload).json()
pprint.pprint(response['data'][0])
print "\nPost count: %d\n" % len(response['data'])

# with specific time
payload['min_timestamp'] = arrow.get(2015, 1, 1).timestamp
payload['max_timestamp'] = arrow.get(2015, 1, 3).timestamp

response = requests.get(endpoint, params=payload).json()
pprint.pprint(response['data'][0])
print "\nPost count: %d\n" % len(response['data'])
