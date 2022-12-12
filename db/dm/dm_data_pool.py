import dmPython
from dbutils.pooled_db import PooledDB

# 自定义Dm连接池
from config import dbInfo
from db.dm.base_dmsql_pool import BaseDmPool
from variables import local_connect


class DmSqlPool(BaseDmPool):
    __dm_pooled = None

    def __init__(self):
        self.conf = dbInfo.get("dm")
        if self.conf is None:
            raise Exception("dm配置文件不存在")
        super(DmSqlPool, self).__init__(**self.conf)

    def get_connection(self):
        if DmSqlPool.__dm_pooled is None:
            DmSqlPool.__dm_pooled = PooledDB(creator=dmPython,  # 数据库类型
                                             maxcached=200,  # 最大空闲数
                                             blocking=True,
                                             # 默认False，即达到最大连接数时，再取新连接将会报错，True，达到最大连接数时，新连接阻塞，等待连接数减少再连接
                                             ping=4,
                                             host=self.host, port=self.port, user=self.user,
                                             password=self.password,
                                             cursorclass=dmPython.DictCursor,  # 游标类型    字典模式
                                             autoCommit=False
                                             )
        return DmSqlPool.__dm_pooled.connection()

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
        if count.rowcount > 0:
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
        if count.rowcount > 0:
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
        if count.rowcount > 0:
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
        return count.rowcount

    def __query(self, sql, param=None):
        _cursor = local_connect.cursor
        if param is None:
            count = _cursor.execute(sql)
        else:
            count = _cursor.execute(sql, param)
        return count.rowcount

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

#
# conn = dm_pooled.connection()
#
# cursor = conn.cursor()
# cursor.execute("select * from test")
# res = cursor.fetchall()
# print(res)
