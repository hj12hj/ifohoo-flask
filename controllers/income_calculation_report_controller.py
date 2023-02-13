from flask import Blueprint

from aop import handle_web_result
from aop.handle_web_request import handle_web_request
from returnmessage import ReturnMessage

# 财司收益测算表
from service import incomeCalculationReportService
from variables import local_token

income_calculation_report = Blueprint("income_calculation_report", __name__)

"""
    财司收益测算表查询
"""


@income_calculation_report.route("/incomeCalculationReport/list", methods=["GET"])
@handle_web_request
@handle_web_result
def get_bond_report_list(**kwargs):
    # params是个不可修改的dict，所以需要新建一个dict添加机构号
    params = kwargs.get("params")
    query_data = {"organCode":local_token.token_info["organCode"]}
    # 遍历赋值
    for key in params:
        query_data[key] = params[key]
    return ReturnMessage(data=incomeCalculationReportService.income_calculation_report_list(query_data))
