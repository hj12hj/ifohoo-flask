import redis


# redis工具类


class RedisUtils:
    def __init__(self, host, port, password, db):
        self.host = host
        self.port = port
        self.password = password
        self.db = db
        self.redis_pool = redis.ConnectionPool(host=host, port=port, password=password, db=db, socket_connect_timeout=1)

    # 获取连接
    def get_connection(self):
        return redis.Redis(connection_pool=self.redis_pool)

    # 获取值
    def get_by_key(self, key):
        info = None
        try:
            info = self.get_connection().get(key).decode("utf-8")
        except Exception as e:
            pass
        return info

    # 测试连接 如果没成功直接终止代码
    def ping_conn(self):
        is_connected = False
        try:
            self.get_connection().ping()
            is_connected = True
        except Exception:
            is_connected = False
        return is_connected


if __name__ == '__main__':
    redis_utils = RedisUtils('10.55.254.135', 6379, '123456', 7)
    print(redis_utils.get_by_key('b469338268174aac9c7b860fd092cabc'))
    # print(redis_utils.get_by_key('test2'))
    # redis_pool = redis.ConnectionPool(host='10.55.254.135', port=6379, password='123456', db=7)
    # redis_conn =
    # a = redis_conn.get('b469338268174aac9c7b860fd092cabc')
    # print(a.decode('UTF8'))
