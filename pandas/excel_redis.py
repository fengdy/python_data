import pandas as pd
import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)
df = pd.read_excel('sal.xls',skiprows=[0])

r.set('dat',df.to_msgpack(compress='zlib',encoding='utf8'))
cf = pd.read_msgpack(r.get('dat'),encoding='utf8')
print cf
