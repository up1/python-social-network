import twitter
import time

api = twitter.Api(consumer_key="xxxxxx",
        consumer_secret="xxxxxx",
        access_token_key="xxxxxx",
        access_token_secret="xxxxxx"
        )

screen_name = "clozed2u"
max_id = None
count = 10

# Get timeline one time
statuses = api.GetUserTimeline(screen_name=screen_name, max_id=max_id, count=count)

# Loop get usertimeline
while True:
    statuses = api.GetUserTimeline(screen_name=screen_name, max_id=max_id, count=count)
    for s in statuses:
        print s.id
        max_id = s.id

    print "ID: %d" % max_id
    time.sleep(5)
