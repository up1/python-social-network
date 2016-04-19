import requests
import pprint
import arrow

api_url = "https://api.instagram.com/v1"
media_id = "765773797587837405_9595407"
endpoint = "%s/media/%s/comments" % (api_url, media_id)

client_id = "xxxxxx"
payload = { 'client_id': client_id }

response = requests.get(endpoint, params=payload).json()
pprint.pprint(response['data'][0])
print "\nComment count: %d\n" % len(response['data'])
