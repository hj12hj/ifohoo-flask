from flask import Blueprint

from aop import handle_web_result
from aop.handle_web_request import handle_web_request
from returnmessage import ReturnMessage

# 保险收益测算表
from service import insuranceProfitCalculationService

insurance_profit_calculation = Blueprint("insurance_profit_calculation", __name__)

"""
    保险收益测算表查询
"""


@insurance_profit_calculation.route("/insuranceProfitCalculation/list", methods=["GET"])
@handle_web_request
@handle_web_result
def get_profit_calculation_report_list(**kwargs):
    print(kwargs.get("params"))
    return ReturnMessage(data=insuranceProfitCalculationService.profit_calculation_report_list(query_data=kwargs.get("params")))
