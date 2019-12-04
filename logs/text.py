import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=12)

r.set('name','zx')
print(r.get('name'))

r.rpush('wl','1','2','3')
print(r.lrange('wl', 0, -1))

r.zadd('game', {'a': 10, 'b': 20, 'c': 15, 'd':20})
print(r.zrevrange('game', 0, -1))
print(r.zrange('game', 0, -1))

import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lufeiapi.settings.dev")
django.setup()


from django.core.cache import cache

cache.set('name', 'bob', 20)
print(cache.get('name'))