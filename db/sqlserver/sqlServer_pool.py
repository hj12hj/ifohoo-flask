# -*- coding: utf-8 -*-
import pymssql
from dbutils.pooled_db import PooledDB
from db.sqlserver.base_pysqlServer_pool import BasePySqlServerPool
from config import dbInfo

"""
上述例子中游标获取的查询结果的每一行为元组类型，
可以通过在创建游标时指定as_dict参数来使游标返回字典变量，
字典中的键为数据表的列名

conn = pymssql.connect(server, user, password, database)
cursor = conn.cursor(as_dict=True)
 
cursor.execute('SELECT * FROM persons WHERE salesrep=%s', 'John Doe')
for row in cursor:
    print("ID=%d, Name=%s" % (row['id'], row['name']))
 
conn.close()
"""


class SqlServerPool(BasePySqlServerPool):
    """
       MYSQL数据库对象，负责产生数据库连接 , 此类中的连接采用连接池实现
           获取连接对象：conn = Mysql.getConn()
           释放连接对象;conn.close()或del conn
       """
    # 连接池对象
    __pool = None

    def __init__(self, conf_name=None):
        self.conf = dbInfo.get("sqlserver")
        if self.conf is None:
            raise Exception("sqlserver")
        super(SqlServerPool, self).__init__(**self.conf)
        # 数据库构造函数，从连接池中取出连接，并生成操作游标
        self._createPool()

    def _createPool(self):
        if not self.dbname:
            raise NameError("没有设置数据库信息")
        self.__pool = PooledDB(creator=pymssql,
                               mincached=2,
                               maxcached=5,
                               maxshared=self.minPoolSize,
                               maxconnections=self.maxPoolSize,
                               blocking=True, host=self.host, user=self.user, password=self.password,
                               database=self.dbname, charset=self.charset)

    def __getConn(self):
        """
        @summary: 静态方法，从连接池中取出连接
        @return MySQLdb.connection
        """
        conn = self.__pool.connection()
        cursor = conn.cursor()
        if not cursor:
            raise Exception("连接数据库失败")
        return cursor

    def execQuery(self, sql, param=None):
        """
        @summary: 执行查询，并取出所有结果集
        @param sql:查询ＳＱＬ，如果有查询条件，请只指定条件列表，并将条件值使用参数[param]传递进来
        @param param: 可选参数，条件列表值（元组/列表）
        @return: result list(字典对象)/boolean 查询到的结果集
        """
        _cursor = self.__getConn()
        if param is None:
            _cursor.execute(sql)
        else:
            _cursor.execute(sql, param)
        result = _cursor.fetchall()
        return result

    def execute(self, sql, param=None):
        """
        @summary: 执行查询，并取出第一条
        @param sql:查询ＳＱＬ，如果有查询条件，请只指定条件列表，并将条件值使用参数[param]传递进来
        @param param: 可选参数，条件列表值（元组/列表）
        @return: result list/boolean 查询到的结果集
        """
        if param is None:
            count = self._cursor.execute(sql)
        else:
            count = self._cursor.execute(sql, param)
        if count > 0:
            result = self._cursor.fetchone()
        else:
            result = False
        return result

    def getMany(self, sql, num, param=None):
        """
        @summary: 执行查询，并取出num条结果
        @param sql:查询ＳＱＬ，如果有查询条件，请只指定条件列表，并将条件值使用参数[param]传递进来
        @param num:取得的结果条数
        @param param: 可选参数，条件列表值（元组/列表）
        @return: result list/boolean 查询到的结果集
        """
        if param is None:
            count = self._cursor.execute(sql)
        else:
            count = self._cursor.execute(sql, param)
        if count > 0:
            result = self._cursor.fetchmany(num)
        else:
            result = False
        return result

    def insertMany(self, sql, values):
        """
        @summary: 向数据表插入多条记录
        @param sql:要插入的ＳＱＬ格式
        @param values:要插入的记录数据tuple(tuple)/list[list]
        @return: count 受影响的行数
        """
        count = self._cursor.executemany(sql, values)
        return count

    def __query(self, sql, param=None):
        if param is None:
            count = self._cursor.execute(sql)
        else:
            count = self._cursor.execute(sql, param)
        return count

    def update(self, sql, param=None):
        """
        @summary: 更新数据表记录
        @param sql: ＳＱＬ格式及条件，使用(%s,%s)
        @param param: 要更新的  值 tuple/list
        @return: count 受影响的行数
        """
        return self.__query(sql, param)

    def insert(self, sql, param=None):
        """
        @summary: 更新数据表记录
        @param sql: ＳＱＬ格式及条件，使用(%s,%s)
        @param param: 要更新的  值 tuple/list
        @return: count 受影响的行数
        """
        return self.__query(sql, param)

    def delete(self, sql, param=None):
        """
        @summary: 删除数据表记录
        @param sql: ＳＱＬ格式及条件，使用(%s,%s)
        @param param: 要删除的条件 值 tuple/list
        @return: count 受影响的行数
        """
        return self.__query(sql, param)

    def begin(self):
        """
        @summary: 开启事务
        """
        self._conn.autocommit(0)

    def end(self, option='commit'):
        """
        @summary: 结束事务
        """
        if option == 'commit':
            self._conn.commit()
        else:
            self._conn.rollback()

    def dispose(self, isEnd=1):
        """
        @summary: 释放连接池资源
        """
        if False not in isEnd:
            self.end('commit')
        else:
            print("sql错误，rollback")
            self.end('rollback')
        self._cursor.close()
        self._conn.close()
