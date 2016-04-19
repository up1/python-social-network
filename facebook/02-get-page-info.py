import requests
import pprint
import arrow

api_url = "https://graph.facebook.com/v2.5"
page_id = "421936097949882"
endpoint = "%s/%s" % (api_url, page_id)

access_token = "xxxxxx"
payload = {
        'access_token': access_token,
        'fields': ','.join(['id', 'name', 'about', 'talking_about_count', 'likes', 'location'])
        }

response = requests.get(endpoint, params=payload).json()
pprint.pprint(response)
