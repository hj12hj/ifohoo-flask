import threading

from flask import request, current_app

from exception.ifms_http_exception import IfmsHttpException
from redisutils import redisutils
from variables.local_page_helper import local_page_info
from variables.local_token import local_token

local_connect = threading.local()


# 本地数据库连接保存用于注解事务
def create_local_connect(app):
    @app.before_request
    def before_request():
        # 验证token
        token = request.headers.get("token")
        if token is None:
            raise IfmsHttpException("token不能为空", 401)
        info = redisutils.get_by_key(token)
        if info is None:
            raise IfmsHttpException("token无效", 401)
        # 绑定线程变量
        from variables.db_connection import db
        conn = db.get_connection()
        local_connect.conn = conn
        local_connect.cursor = conn.cursor()
        local_token.token = request.headers.get("token")

        try:
            params = request.args
        except Exception as e:
            params = None
        # 解析请求参数里的分页信息 用于后续sql 拦截 拼接
        if params is not None:
            if request.method == "GET":
                try:
                    local_page_info.pageNum = params.get("pageNum")
                    local_page_info.pageSize = params.get("pageSize")
                except Exception as e:
                    pass

    # 这里归还数据库连接池
    @app.after_request
    def after_request(response):
        is_has = False
        try:
            local_connect.__getattribute__("conn")
            is_has = True
        except Exception:
            is_has = False
        if is_has:
            local_connect.conn.close()
            local_connect.cursor.close()
            local_connect.conn = None
            local_connect.cursor = None

        return response

    @app.errorhandler(Exception)
    def server_error(e):
        current_app.logger.error("访问出错 ---->  " + str(e))
        msg = {
            "code": -1,
            "msg": e.__str__()
        }
        if isinstance(e, IfmsHttpException):
            return e.__str__()
        else:
            return msg
