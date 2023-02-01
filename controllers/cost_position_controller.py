from flask import Blueprint

from aop import handle_web_result
from aop.handle_web_request import handle_web_request
from feign.data_center_feign_client import findCurrencyMap
from returnmessage import ReturnMessage
from service import costPositionService

# 每日持仓
cost_position = Blueprint("cost_position", __name__)

"""
    每日持仓列表查询
"""


@cost_position.route("/costPosition/list", methods=["GET"])
@handle_web_request
@handle_web_result
def get_config_history_list(**kwargs):
    return ReturnMessage(data=costPositionService.get_cost_position_list(query_data=kwargs.get("params")))
