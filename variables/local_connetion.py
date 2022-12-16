import logging
import threading

from flask import request, current_app

from exception.ifms_http_exception import IfmsHttpException
from variables.local_page_helper import local_page_info
from variables.local_token import local_token

local_connect = threading.local()

# 本地数据库连接保存用于注解事务
def create_local_connect(app):
    from registry import config
    from config import logToFile
    if config is not None and config["logToFile"] is not None:
        log_file_flag = config["logToFile"]
    else:
        log_file_flag = logToFile
    """
       flask log
    """
    if log_file_flag == True:
        # 添加控制台handler，用于输出日志到控制台
        console_handler = logging.StreamHandler()
        # 添加日志文件handler，用于输出日志到文件中
        file_handler = logging.FileHandler(filename='log.log', encoding='UTF-8')
        # 设置格式并赋予handler
        formatter = logging.Formatter(
            "%(asctime)s %(name)s:%(levelname)s:%(message)s   in files %(filename)s: lines %(lineno)s")
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        # 将handler添加到日志器中
        app.logger.addHandler(file_handler)
        # app.logger.addHandler(console_handler)
        app.logger.setLevel(logging.DEBUG)

    @app.before_request
    def before_request():
        # 绑定线程变量
        from variables.db_connection import db
        conn = db.get_connection()
        local_connect.conn = conn
        local_connect.cursor = conn.cursor()

        try:
            params = request.args
        except Exception as e:
            params = None
        # 解析请求参数里的分页信息 用于后续sql 拦截 拼接
        if params is not None:
            if request.method == "GET":
                try:
                    local_page_info.pageNum = int(params.get("page"))
                    local_page_info.pageSize = int(params.get("pagesize"))
                    app.logger.info("拦截到分页请求 pageNum = " + str(local_page_info.pageNum) + " pageSize = " + str(
                        local_page_info.pageSize))
                except Exception as e:
                    pass

    # 这里归还数据库连接池
    @app.teardown_request
    def after_request(request):
        is_has = False
        try:
            local_connect.__getattribute__("conn")
            is_has = True
        except Exception as e:
            is_has = False
        if is_has:
            local_connect.conn.close()
            local_connect.cursor.close()
            local_connect.conn = None
            local_connect.cursor = None

    @app.errorhandler(Exception)
    def server_error(e):
        current_app.logger.error("访问出错 ---->  " + str(e))
        msg = {
            "code": -1,
            "message": e.__str__()
        }
        if isinstance(e, IfmsHttpException):
            return e.__str__()
        else:
            return msg
