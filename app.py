import logging

from flask import Flask
from flask.logging import default_handler
from controllers import blueprint_list
from registry import port
from variables.local_connetion import create_local_connect

app = Flask(__name__)
serverPort = port if port is not None else 5000


def logger_config():
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
    app.logger.removeHandler(default_handler)
    default_handler.setFormatter(formatter)


# 注册蓝图列表
for blueprint in blueprint_list:
    app.register_blueprint(blueprint)

if __name__ == '__main__':
    logger_config()
    app.logger.warning(
        """
        ----------------------------
        |  app.run() => flask run  |
        ----------------------------
        """
    )
    create_local_connect(app)
    app.run(debug=False, port=serverPort, host='0.0.0.0')
