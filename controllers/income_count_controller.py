from flask import Blueprint

from aop import handle_web_result
from aop.handle_web_request import handle_web_request
from returnmessage import ReturnMessage

# 收益率计算报表
from service import incomeCountReportService

incomeCount_report = Blueprint("incomeCount_report", __name__)

"""
    收益率计算报表列表查询
"""


@incomeCount_report.route("/incomeCountReport/list", methods=["GET"])
@handle_web_request
@handle_web_result
def get_incomeCount_report_list(**kwargs):
    return ReturnMessage(data=incomeCountReportService.incomeCount_report_list(query_data=kwargs.get("params")))
