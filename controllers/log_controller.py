from flask import Blueprint

from aop import handle_web_result
from feign.log_feign_client import hh
from aop.handle_web_request import handle_web_request
from returnmessage import ReturnMessage
from service import userService
from flask import Blueprint, current_app

from aop import handle_web_result
from aop.handle_web_request import handle_web_request
from feign.log_feign_client import hh
from returnmessage import ReturnMessage
from service import userService

# 注册蓝图
log = Blueprint("log", __name__)


# 具体各个controller方法
# 这里的 kwargs {params:"",json_data:"",headers:""} 是 透传的对象 函数参数必须带上不然报错
@log.route("/log", methods=["GET"])
@handle_web_request
@handle_web_result
def testGet(**kwargs):
    list = userService.get_all()
    userService.insert_user()
    return ReturnMessage(data=list)


@log.route("/test", methods=["GET"])
@handle_web_request
def testPost(**kwargs):
    print(hh(json={"name": "hh", "age": 18}))
    return "log"
