import redis 

cmaster = redis.StrictRedis(host="127.0.0.1", port=6379,db=0,password="abcd1234")

cmaster.set('diogo',200)
