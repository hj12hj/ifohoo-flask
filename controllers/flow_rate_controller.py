from flask import Blueprint

from aop import handle_web_result
from aop.handle_web_request import handle_web_request
from returnmessage import ReturnMessage

# 综合流动比率报表
from service import flowRateReportService

flowRate_report = Blueprint("flowRate_report", __name__)

"""
    综合流动比率报表列表查询
"""


@flowRate_report.route("/flowRateReport/list", methods=["GET"])
@handle_web_request
@handle_web_result
def get_flowRate_report_list(**kwargs):
    return ReturnMessage(data=flowRateReportService.flowRate_report_list(query_data=kwargs.get("params")))
