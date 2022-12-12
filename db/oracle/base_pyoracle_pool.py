
class BasePyOraclePool(object):
    def __init__(self, host,port, sid,username, password,charset="utf8", dbname=None,min_pool_size=1,max_pool_size=20):
        self.host = host
        self.port = int(port)
        self.user = username
        self.sid=sid
        self.password = str(password)
        self.charset=charset
        self.dbname = dbname
        self.minPoolSize=min_pool_size
        self.maxPoolSize=max_pool_size
        self.conn = None
        self.cursor = None

