
class BasePymysqlPool(object):
    def __init__(self, host, port, username, password, dbname,charset="utf8",min_pool_size=1,max_pool_size=20):
        self.db_host = host
        self.db_port = int(port)
        self.user = username
        self.password = str(password)
        self.db = dbname
        self.minPoolSize=min_pool_size
        self.charset=charset
        self.maxPoolSize=max_pool_size
        self.conn = None
        self.cursor = None


    def test_connect(self):
        pass