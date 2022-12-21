import cx_Oracle

from db.common_db_pool_base import CommonDbPoolBase
from variables.local_connetion import local_connect
from flask import current_app
import re
from variables.local_page_helper import local_page_info


# 通用数据库连接池实现类
class CommonDbPool(CommonDbPoolBase):
    def __init__(self, db_type, db_config):
        super(CommonDbPool, self).__init__(db_type, db_config)

    # 查询单个结果
    def query_one(self, sql, data=None):
        current_app.logger.info("查询单个结果 sql --> " + sql)
        current_app.logger.info("参数 --> " + str(data))
        conn = local_connect.conn
        cursor = conn.cursor()
        if data is None:
            cursor.execute(sql)
        else:
            # mysql 占位符跟 oracle dm  不一样 加个转换
            if self.db_type == "mysql":
                sql = re.sub(":\d{1,2}", "%s", sql)
            cursor.execute(sql, data)
        fetch_data = cursor.fetchone()
        fields = [tup[0] for tup in cursor.description]
        fields = [self.__str2Hump(i) for i in fields]
        if fetch_data is None:
            return None
        else:
            data = dict(zip(fields, fetch_data))
            if self.db_type == "oracle":
                # oracle clob
                for key, value in data.items():
                    if isinstance(value, self.db_creator.LOB):
                        data[key] = value.read()
            return data

    # 查询所有结果
    def query_all(self, sql, data=None):
        current_app.logger.info("查询多个结果 sql --> " + sql)
        current_app.logger.info("参数 --> " + str(data))
        conn = local_connect.conn
        cursor = conn.cursor()
        if data is None:
            cursor.execute(sql)
        else:
            # mysql 占位符跟 oracle dm  不一样 加个转换
            if self.db_type == "mysql":
                sql = re.sub(":\d{1,2}", "%s", sql)
            cursor.execute(sql, data)
        fetch_data = cursor.fetchall()
        fields = [tup[0] for tup in cursor.description]
        fields = [self.__str2Hump(i) for i in fields]
        if fetch_data is None:
            return None
        else:
            data = [dict(zip(fields, row)) for row in fetch_data]
            if self.db_type == "oracle":
                # oracle clob
                for return_data in data:
                    for key, value in return_data.items():
                        if isinstance(value, self.db_creator.LOB):
                            return_data[key] = value.read()
            return data

    # 查询指定个数结果
    def query_many(self, sql, data=None, num=0):
        current_app.logger.info("查询多个结果 sql --> " + sql)
        current_app.logger.info("参数 --> " + str(data))
        conn = local_connect.conn
        cursor = conn.cursor()
        if data is None:
            cursor.execute(sql)
        else:
            # mysql 占位符跟 oracle dm  不一样 加个转换
            if self.db_type == "mysql":
                sql = re.sub(":\d{1,2}", "%s", sql)
            cursor.execute(sql, data)
        fetch_data = cursor.fetchmany(num)
        fields = [tup[0] for tup in cursor.description]
        fields = [self.__str2Hump(i) for i in fields]
        if fetch_data is None:
            return None
        else:
            data = [dict(zip(fields, row)) for row in fetch_data]
            if self.db_type == "oracle":
                # oracle clob
                for return_data in data:
                    for key, value in return_data.items():
                        if isinstance(value, self.db_creator.LOB):
                            return_data[key] = value.read()
            return data

    # 分页查询
    def query_page(self, sql, data=None, handle_none=False):
        current_app.logger.info("分页查询 sql --> " + sql)
        conn = local_connect.conn
        cursor = conn.cursor()
        page_num = 1
        page_size = 10
        try:
            page_size = local_page_info.pageSize
            page_num = local_page_info.pageNum
        except Exception:
            pass
        if data is None:
            # 正则得到求总数的sql
            all_sql = self.__handle_limit_sql(sql)
            if self.db_type == "mysql" or self.db_type == "dm":
                if self.db_type == "mysql":
                    sql = re.sub(":\d{1,2}", "%s", sql)
                cursor.execute(all_sql)
                all_count = cursor.fetchone()[0]
                current_app.logger.info(self.db_type + "分页查询所有数据" + all_sql)
                limit_sql = sql + " limit " + str((page_num - 1) * page_size) + "," + str(page_size)
                cursor.execute(limit_sql)
                current_app.logger.info(self.db_type + "分页查询分页数据" + limit_sql)
                current_app.logger.info(self.db_type + "分页查询分页参数" + str(data))
                fetch_data = cursor.fetchall()
                fields = [tup[0] for tup in cursor.description]
                fields = [self.__str2Hump(i) for i in fields]
                return all_count, [dict(zip(fields, row)) for row in fetch_data]
            elif self.db_type == "oracle":
                # oracle 分页拦截
                cursor.execute(all_sql)
                all_count = cursor.fetchone()[0]
                current_app.logger.info(self.db_type + "分页查询所有数据" + all_sql)
                limit_sql = "select * from (select rownum rn, t.* from (" + sql + ") t where rownum <= " + str(
                    page_num * page_size) + ") where rn > " + str((page_num - 1) * page_size)
                cursor.execute(limit_sql)
                current_app.logger.info(self.db_type + "分页查询分页数据" + limit_sql)
                current_app.logger.info(self.db_type + "分页查询分页参数" + str(data))
                fetch_data = cursor.fetchall()
                fields = [tup[0] for tup in cursor.description]
                fields = [self.__str2Hump(i) for i in fields]
                return all_count, [dict(zip(fields, row)) for row in fetch_data]
            else:
                raise Exception("分页查询不支持数据库类型！！！")
        else:
            # 处理查询条件为空情况
            if handle_none:
                sql, data = self.__handle_query_str(sql, data)
            # 正则得到求总数的sql
            all_sql = self.__handle_limit_sql(sql)
            if self.db_type == "mysql" or self.db_type == "dm":
                # mysql 占位符跟 oracle dm  不一样 加个转换
                if self.db_type == "mysql":
                    sql = re.sub(":\d{1,2}", "%s", sql)
                    all_sql = re.sub(":\d{1,2}", "%s", all_sql)
                cursor.execute(all_sql, data)
                all_count = cursor.fetchone()[0]
                current_app.logger.info(self.db_type + "分页查询所有数据" + all_sql)
                limit_sql = sql + " limit " + str((page_num - 1) * page_size) + "," + str(page_size)
                current_app.logger.info(self.db_type + "分页查询分页数据" + limit_sql)
                current_app.logger.info(self.db_type + "分页查询所有参数" + str(data))
                cursor.execute(limit_sql, data)
                fetch_data = cursor.fetchall()
                fields = [tup[0] for tup in cursor.description]
                fields = [self.__str2Hump(i) for i in fields]
                return all_count, [dict(zip(fields, row)) for row in fetch_data]
            elif self.db_type == "oracle":
                # oracle 分页拦截
                cursor.execute(all_sql, data)
                all_count = cursor.fetchone()[0]
                current_app.logger.info(self.db_type + "分页查询所有数据" + all_sql)
                limit_sql = "select * from (select rownum rn, t.* from (" + sql + ") t where rownum <= " + str(
                    page_num * page_size) + ") where rn > " + str((page_num - 1) * page_size)
                cursor.execute(limit_sql, data)
                current_app.logger.info(self.db_type + "分页查询分页数据" + limit_sql)
                current_app.logger.info(self.db_type + "分页查询分页参数" + str(data))
                fetch_data = cursor.fetchall()
                fields = [tup[0] for tup in cursor.description]
                fields = [self.__str2Hump(i) for i in fields]
                data = [dict(zip(fields, row)) for row in fetch_data]
                # oracle clob
                for return_data in data:
                    for key, value in return_data.items():
                        if isinstance(value, self.db_creator.LOB):
                            return_data[key] = value.read()
                return all_count, data

            else:
                raise Exception("分页查询不支持数据库类型！！！")

    # 执行单个sql insert update delete
    def execute_sql(self, sql, data=None):
        current_app.logger.info("执行单个sql语句 sql --> " + sql)
        current_app.logger.info("参数 --> " + str(data))
        conn = local_connect.conn
        cursor = conn.cursor()
        if data is None:
            cursor.execute(sql)
        else:
            if self.db_type == "mysql":
                sql = re.sub(":\d{1,2}", "%s", sql)
            cursor.execute(sql, data)

    # 执行单个多个
    def insert_many(self, sql, values):
        conn = local_connect.conn
        cursor = conn.cursor()
        if self.db_type == "mysql":
            sql = re.sub(":\d{1,2}", "%s", sql)
        cursor.executemany(sql, values)

    # 驼峰转换
    def __str2Hump(self, text):
        text = text.lower()
        arr = filter(None, text.lower().split('_'))
        res = ''
        j = 0
        for i in arr:
            if j == 0:
                res = i
            else:
                res = res + i[0].upper() + i[1:]
            j += 1
        return res

    # 查询参数处理  去了 查询条件为 None 的情况  todo  待优化
    def __handle_query_str(self, sql, param):
        current_app.logger.info("处理sql查询条件")
        current_app.logger.info("param --> " + str(param))
        length = len(param)
        new_list = []
        for i in range(1, length):
            if param[i] is None or param[i] == '':
                sql = re.sub("and [^0-9]*[=,<,>,like]:" + str(i + 1), " ", sql)
            else:
                new_list.append(param[i])
        if param[0] is None or param[0] == '':
            if len(new_list) == 0:
                sql = re.sub("where.*?.*?:1.*?", " ", sql)
            elif len(new_list) != 0:
                sql = re.sub("where.*?.*?:1.*?and", "where ", sql)
        else:
            new_list.insert(0, param[0])
        current_app.logger.info("处理后的sql --> " + sql)
        current_app.logger.info("处理后的参数 --> " + str(new_list))
        return sql, new_list

    # 分页处理
    def __handle_limit_sql(self, sql):
        match = re.match(".*(from.*)", sql)
        if match is None:
            raise Exception("分页查询拦截sql语句出错")
        else:
            from_sql = match.group(1)
            all_sql = "select count(*)  " + match.group(1)

        return all_sql
