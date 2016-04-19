import redis
import json

r = redis.StrictRedis(host='docker.local', port=6379, db=0)

users = [
        {'username': 'clozed2u', 'full_name': 'lattapon yodsuwan', 'age': '25'},
        {'username': 'teamofz', 'full_name': 'pattapong cherthong', 'age': '25'},
        {'username': 'thangman22', 'full_name': 'warat wongmaneekit', 'age': '26'}
        ]

# Push data to list
for user in users:
    print "Push %s to list" % user['username']
    r.rpush('users', json.dumps(user))

print "Current data length in list: %d" % r.llen('users')

# Show data in list
print "Current data in list: %s" % r.lrange('users', 0, -1)

# Pop data from list
while r.llen('users') > 0:
    print "Get info for user: %s" % json.loads(r.lpop('users'))['username']
