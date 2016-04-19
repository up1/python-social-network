import twitter
import time

api = twitter.Api(consumer_key="xxxxxx",
        consumer_secret="xxxxxx",
        access_token_key="xxxxxx",
        access_token_secret="xxxxxx"
        )

results = api.GetSearch(term="#twitter", count=100)
for s in results:
    print s.created_at
    print s.id
    print s.text
