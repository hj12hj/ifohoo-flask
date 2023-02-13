from flask import Blueprint

from aop import handle_web_result
from aop.handle_web_request import handle_web_request
from returnmessage import ReturnMessage

# 短期报表
from service import assetDetailReportService

assetDetail_report = Blueprint("assetDetail_report", __name__)

"""
    资产明细列表查询
"""


@assetDetail_report.route("/assetDetail/list", methods=["GET"])
@handle_web_request
@handle_web_result
def get_assetDetail_report_list(**kwargs):
    return ReturnMessage(data=assetDetailReportService.assetDetail_report_list(query_data=kwargs.get("params")))