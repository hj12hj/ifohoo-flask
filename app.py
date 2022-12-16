import json
import socket

from flask import Flask, request
# from gevent import pywsgi
from controllers import blueprint_list
from exception.ifms_http_exception import IfmsHttpException
from redisutils import redisutils
from registry import port
from variables import local_token
from variables.local_connetion import create_local_connect

# import pymysql
# import cx_Oracle
# import dmPython


app = Flask(__name__)
serverPort = port if port is not None else 5000


# 检查端口是否被占用 自动切换
def port_is_used(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('127.0.0.1', port))
    return result == 0  # 0 open 1 close


@app.before_request
def before_request():
    # 验证token
    token = request.headers.get("token")
    local_token.token = request.headers.get("token")
    if token is None:
        raise IfmsHttpException("token不能为空", 401)
    info = redisutils.get_by_key(token)
    if info is None:
        raise IfmsHttpException("token无效", 401)
    else:
        # 存储token信息
        local_token.token_info = json.loads(info)


# 注册蓝图列表
for blueprint in blueprint_list:
    app.register_blueprint(blueprint)

if __name__ == '__main__':
    app.logger.warning(
        """
        ----------------------------
        |  app.run() => flask run  | 
        ----------------------------
        """
    )
    create_local_connect(app)
    # server = pywsgi.WSGIServer(('0.0.0.0', serverPort), app)
    # 检查端口占用切换
    # for i in range(serverPort - 1, 65535):
    #     if not port_is_used(i):
    #         serverPort = i
    #         break
    # server.serve_forever()
    app.run(debug=False, port=serverPort, host='0.0.0.0')
