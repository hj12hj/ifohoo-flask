import abc
from dbutils.pooled_db import PooledDB
import importlib


# 通用数据库连接池抽象类
class CommonDbPoolBase(metaclass=abc.ABCMeta):

    def __init__(self, db_type, db_config):
        self.db_type = db_type
        self.db_creator = None
        if self.db_type == "mysql":
            self.db_creator = importlib.import_module("pymysql")
        elif self.db_type == "sqlserver":
            self.db_creator = importlib.import_module("pymssql")
        elif self.db_type == "oracle":
            self.db_creator = importlib.import_module("cx_Oracle")
            # 加入本地驱动包
            # self.db_creator.init_oracle_client(lib_dir="/Users/hejie/Documents/instantclient_19_8")
        elif self.db_type == "dm":
            self.db_creator = importlib.import_module("dmPython")
        else:
            raise Exception("unsupported database type " + self.db_type)

        self.pool = PooledDB(self.db_creator,
                             mincached=0,
                             maxcached=6,
                             maxconnections=0,
                             blocking=True,
                             ping=0,
                             **db_config)

    # 获取连接
    def get_connection(self):
        return self.pool.connection()

    # 测试是否连接成功
    def is_connection(self):
        is_connection = False
        try:
            self.get_connection().cursor().execute("select 1 from dual")
            is_connection = True
        except Exception as e:
            print(e)
            is_connection = False
        return is_connection

    # 查询单个结果
    @abc.abstractmethod
    def query_one(self, sql, data=None):
        pass

    # 查询所有结果
    @abc.abstractmethod
    def query_all(self, sql, data=None):
        pass

    # 查询指定个数结果
    @abc.abstractmethod
    def query_many(self, sql, data=None, num=0):
        pass

    # 分页查询
    @abc.abstractmethod
    def query_page(self, sql, data=None):
        pass

    # 执行单个sql insert update delete
    @abc.abstractmethod
    def execute_sql(self, sql, data=None):
        pass

    # 执行单个多个
    @abc.abstractmethod
    def insert_many(self, sql, values):
        pass
