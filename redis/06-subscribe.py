import redis
import json
import sys

channel = sys.argv[1]

r = redis.Redis(host='docker.local')
p = r.pubsub()
p.subscribe(channel)
print "Subscribe to channel: %s" % channel

while True:
    for message in p.listen():
        try:
            message = json.loads(message['data'])
            print "%s: %s" % (message['user'], message['message'])
        except:
            pass
