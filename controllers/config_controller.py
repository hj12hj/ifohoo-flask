from flask import Blueprint

from aop import handle_web_result
from aop.handle_web_request import handle_web_request
from returnmessage import ReturnMessage
from service import configService

# 动态报表配置 config
config = Blueprint("config", __name__)


# 查询列表
@config.route("/config/list", methods=["GET"])
@handle_web_request
@handle_web_result
def get_list(**kwargs):
    query_params = kwargs["params"]
    return ReturnMessage(data=configService.get_config_list(query_params))


# 插入数据
@config.route("/config/insert", methods=["POST"])
@handle_web_request
@handle_web_result
def insert_config(**kwargs):
    json_data = kwargs.get("json_data")
    configService.insert_config_info(json_data)
    return ReturnMessage()


# 更新数据
@config.route("/config/update", methods=["POST"])
@handle_web_request
@handle_web_result
def update_config(**kwargs):
    json_data = kwargs.get("json_data")
    configService.update_config_info(json_data)
    return ReturnMessage()
