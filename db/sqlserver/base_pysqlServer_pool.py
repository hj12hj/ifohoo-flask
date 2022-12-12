class BasePySqlServerPool(object):
    def __init__(self, host, port, username, password, charset="GBK", dbname=None, min_pool_size=1, max_pool_size=20):
        self.host = host
        self.port = int(port)
        self.user = username
        self.password = str(password)
        self.dbname = dbname
        self.charset = charset
        self.minPoolSize = min_pool_size
        self.maxPoolSize = max_pool_size
        self.conn = None
        self.cursor = None
