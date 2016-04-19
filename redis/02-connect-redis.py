import redis

r = redis.StrictRedis(host='docker.local', port=6379, db=0) # redis.Redis work the same
