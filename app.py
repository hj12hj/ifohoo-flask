import logging

from flask import Flask
from flask.logging import default_handler
from controllers import blueprint_list
from registry import port
from variables.local_connetion import create_local_connect

app = Flask(__name__)
serverPort = port if port is not None else 5000




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
