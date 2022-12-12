import redisutils
from redisutils.redis_utils import RedisUtils
from config import redisConfig

redisutils = RedisUtils(**redisConfig)
print("redis_config_is  ---->>>>  "+str(redisConfig))
is_conn = redisutils.ping_conn()

if is_conn == False:
    raise Exception("redis is not connected!!!")
