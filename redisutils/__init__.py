import redisutils
from redisutils.redis_utils import RedisUtils
from config import redisConfig
from registry import config

if config is None:
    redisutils = RedisUtils(**redisConfig)
    print("local_redis_config_is  ---->>>>  " + str(redisConfig))
else:
    redisConfig = config.get("redis")
    redisutils = RedisUtils(**redisConfig)
    print("remote_redis_config_is  ---->>>>  " + str(redisConfig))

is_conn = redisutils.ping_conn()

if is_conn == False:
    raise Exception("redis is not connected!!!")
