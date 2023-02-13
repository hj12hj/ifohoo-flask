from flask import Blueprint

from aop import handle_web_result
from aop.handle_web_request import handle_web_request
from returnmessage import ReturnMessage

# 现金流测试报表
from service import cashTestReportService

cashTest_report = Blueprint("cashTest_report", __name__)

"""
    现金流测试报表列表查询
"""


@cashTest_report.route("/cashTestReport/list", methods=["GET"])
@handle_web_request
@handle_web_result
def get_cashTest_report_list(**kwargs):
    return ReturnMessage(data=cashTestReportService.cashTest_report_list(query_data=kwargs.get("params")))
