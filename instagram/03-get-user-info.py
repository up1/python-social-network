import requests
import pprint

api_url = "https://api.instagram.com/v1"
user_id = "9595407"
endpoint = "%s/users/%s" % (api_url, user_id)

client_id = "xxxxxx"
payload = { 'client_id': client_id }

pprint.pprint(requests.get(endpoint, params=payload).json())
