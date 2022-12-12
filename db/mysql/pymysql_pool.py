import pymysql
from dbutils.pooled_db import PooledDB
from pymysql.cursors import DictCursor
from variables.local_page_helper import local_page_info
from config import dbInfo
from db.mysql.base_pymysql_pool import BasePymysqlPool
from variables.local_connetion import local_connect


class PyMysqlPool(BasePymysqlPool):

    def test_connect(self):
        try:
            self.get_connection().cursor().execute("select 1")
            return True
        except Exception as e:
            return False

    """
    MYSQL数据库对象，负责产生数据库连接 , 此类中的连接采用连接池实现
        获取连接对象：conn = Mysql.getConn()
        释放连接对象;conn.close()或del conn
    """
    # 连接池对象
    __pool = None

    def __init__(self, conf_name=None):
        # self.conf = {'host': '127.0.0.1', 'port': 3306, 'username': 'root', 'password': 'hj123456', 'dbname': 'test',
        #              'charset': 'utf8'}
        self.conf = dbInfo.get("mysql")
        if self.conf is None:
            raise Exception("mysql配置文件不存在")
        super(PyMysqlPool, self).__init__(**self.conf)

    def get_connection(self):
        """
        @summary: 静态方法，从连接池中取出连接
        @return MySQLdb.connection
        """
        if PyMysqlPool.__pool is None:
            __pool = PooledDB(creator=pymysql,
                              mincached=self.minPoolSize,
                              maxcached=self.maxPoolSize,
                              host=self.db_host,
                              port=self.db_port,
                              user=self.user,
                              passwd=self.password,
                              db=self.db,
                              use_unicode=True,
                              charset=self.charset,
                              cursorclass=DictCursor)
        return __pool.connection()

    def getAll(self, sql, param=None):
        _cursor = local_connect.cursor
        # totalCount = None
        # pageNum = local_page_info.pageNum
        # pageSize = local_page_info.pageSize
        # limitSql = sql + " limit " + pageNum + "," + pageSize
        """
        @summary: 执行查询，并取出所有结果集
        @param sql:查询ＳＱＬ，如果有查询条件，请只指定条件列表，并将条件值使用参数[param]传递进来
        @param param: 可选参数，条件列表值（元组/列表）
        @return: result list(字典对象)/boolean 查询到的结果集
        """
        if param is None:
            count = _cursor.execute(sql)
            # count = _cursor.execute(limitSql)
        else:
            count = _cursor.execute(sql, param)
        if count > 0:
            result = _cursor.fetchall()
        else:
            result = False
        return result

    def getOne(self, sql, param=None):
        _cursor = local_connect.cursor
        """
        @summary: 执行查询，并取出第一条
        @param sql:查询ＳＱＬ，如果有查询条件，请只指定条件列表，并将条件值使用参数[param]传递进来
        @param param: 可选参数，条件列表值（元组/列表）
        @return: result list/boolean 查询到的结果集
        """
        if param is None:
            count = _cursor.execute(sql)
        else:
            count = _cursor.execute(sql, param)
        if count > 0:
            result = _cursor.fetchone()
        else:
            result = False
        return result

    def getMany(self, sql, num, param=None):
        _cursor = local_connect.cursor
        """
        @summary: 执行查询，并取出num条结果
        @param sql:查询ＳＱＬ，如果有查询条件，请只指定条件列表，并将条件值使用参数[param]传递进来
        @param num:取得的结果条数
        @param param: 可选参数，条件列表值（元组/列表）
        @return: result list/boolean 查询到的结果集
        """
        if param is None:
            count = _cursor.execute(sql)
        else:
            count = _cursor.execute(sql, param)
        if count > 0:
            result = _cursor.fetchmany(num)
        else:
            result = False
        return result

    def insertMany(self, sql, values):
        _cursor = local_connect.cursor
        """
        @summary: 向数据表插入多条记录
        @param sql:要插入的ＳＱＬ格式
        @param values:要插入的记录数据tuple(tuple)/list[list]
        @return: count 受影响的行数
        """
        count = _cursor.executemany(sql, values)
        return count

    def __query(self, sql, param=None):
        _cursor = local_connect.cursor
        if param is None:
            count = _cursor.execute(sql)
        else:
            count = _cursor.execute(sql, param)
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
        _conn = local_connect.conn
        """
        @summary: 开启事务
        """
        _conn.autocommit(0)

    def end(self, option='commit'):
        _conn = local_connect.conn
        """
        @summary: 结束事务
        """
        if option == 'commit':
            _conn.commit()
        else:
            _conn.rollback()

    # def dispose(self, isEnd=1):
    #     """
    #     @summary: 释放连接池资源
    #     """
    #     if False not in isEnd:
    #         self.end('commit')
    #     else:
    #         print("sql错误，rollback")
    #         self.end('rollback')
    #     self._cursor.close()
    #     self._conn.close()
