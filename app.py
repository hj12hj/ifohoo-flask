from flask import Flask, request

from controllers import blueprint_list
from exception.ifms_http_exception import IfmsHttpException
from registry import port
from variables.local_connetion import create_local_connect
from redisutils import redisutils

app = Flask(__name__)
serverPort = port if port is not None else 5000


@app.before_request
def before_request():
    # 验证token
    token = request.headers.get("token")
    if token is None:
        raise IfmsHttpException("token不能为空", 401)
    info = redisutils.get_by_key(token)
    if info is None:
        raise IfmsHttpException("token无效", 401)

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
    app.run(debug=False, port=serverPort, host='0.0.0.0')
