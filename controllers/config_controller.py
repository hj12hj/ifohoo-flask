from flask import Blueprint

from aop import handle_web_result
from aop.handle_web_request import handle_web_request
from feign.log_feign_client import hh
from returnmessage import ReturnMessage
from service import userService

# config
config = Blueprint("config", __name__)



