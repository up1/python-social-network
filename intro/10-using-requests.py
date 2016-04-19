import requests

endpoint = "https://api.github.com"

response = requests.get(endpoint)
if response.status_code is 200:
    dict_response = response.json() # Convert response to json
    for k, v in dict_response.iteritems():
        print "%s: %s" % (k, v)
else:
    print "Cannot fetch data from api"
