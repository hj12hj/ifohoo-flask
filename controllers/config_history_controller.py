from flask import Blueprint

from aop import handle_web_result
from aop.handle_web_request import handle_web_request
from returnmessage import ReturnMessage
from service import historyService

# 注册蓝图
config_history = Blueprint("config_history", __name__)


# 具体各个controller方法
# 这里的 kwargs {params:"",json_data:"",headers:""} 是 透传的对象 函数参数必须带上不然报错
@config_history.route("/configHistory/list", methods=["GET"])
@handle_web_request
@handle_web_result
def get_config_history_list(**kwargs):
    return ReturnMessage(data=historyService.get_config_history_list(query_data=kwargs.get("params")))


@config_history.route("/configHistory/latestConfig", methods=["GET"])
@handle_web_request
@handle_web_result
def find_latest_config(**kwargs):
    return ReturnMessage(data=historyService.find_latest_history(query_data=kwargs.get("params")))
