import redis
import json
import sys

user = sys.argv[1]
channel = sys.argv[2]

data = { 'user': user, 'message': '' }

r = redis.Redis(host='docker.local')

while True:
    input_message = raw_input("Enter message: ")
    data['message'] = input_message
    r.publish(channel, json.dumps(data))
