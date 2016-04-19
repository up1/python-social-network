import redis
import json

info = {
        'user': 'clozed2u',
        'full_name': 'lattapon yodsuwan',
        'age': '25'
        }

r = redis.StrictRedis(host='docker.local', port=6379, db=0)

# Set key to value
r.set('lattapon', json.dumps(info))

# Get value from key
print r.get('lattapon')
