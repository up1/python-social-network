import twitter
import pprint
import json

api = twitter.Api(consumer_key="xxxxxx",
        consumer_secret="xxxxxx",
        access_token_key="xxxxxx",
        access_token_secret="xxxxxx"
        )

info = api.GetUser(screen_name='clozed2u')
# print info
print info.name
print info.screen_name
print info.description
print info.statuses_count
