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
    return ReturnMessage(data=configService.get_config_list(kwargs["params"]))


# 插入数据
@config.route("/config/add", methods=["POST"])
@handle_web_request
@handle_web_result
def insert_config(**kwargs):
    json_data = kwargs.get("json_data")
    configService.insert_config_info(json_data)
    return ReturnMessage()


@config.route("/config/delete", methods=["POST"])
@handle_web_request
@handle_web_result
def delete_by_id(**kwargs):
    params = kwargs.get("json_data")
    configService.delete_by_id(params.get("formCode"))
    return ReturnMessage()


# 更新数据
@config.route("/config/update", methods=["POST"])
@handle_web_request
@handle_web_result
def update_config(**kwargs):
    json_data = kwargs.get("json_data")
    configService.update_config_info(json_data)
    return ReturnMessage()


# 部署配置
@config.route("/config/publish", methods=["POST"])
@handle_web_request
@handle_web_result
def deploy_config(**kwargs):
    params = kwargs.get("json_data")
    configService.deploy_config(params.get("formCode"))
    return ReturnMessage()


# 详情
@config.route("/config/findOne", methods=["GET"])
@handle_web_request
@handle_web_result
def find_by_id(**kwargs):
    params = kwargs.get("params")
    configService.find_by_id(params.get("formCode"))
    return ReturnMessage()


# Map
@config.route("/config/nameMap", methods=["GET"])
@handle_web_request
@handle_web_result
def find_name_map(**kwargs):
    data = configService.find_name_map()
    return ReturnMessage(data=data)
