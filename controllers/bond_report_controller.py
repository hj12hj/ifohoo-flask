from flask import Blueprint

from aop import handle_web_result
from aop.handle_web_request import handle_web_request
from returnmessage import ReturnMessage

# 短期报表
from service import bondReportService

bond_report = Blueprint("bond_report", __name__)

"""
    短期报表列表查询
"""


@bond_report.route("/bondReport/list", methods=["GET"])
@handle_web_request
@handle_web_result
def get_bond_report_list(**kwargs):
    return ReturnMessage(data=bondReportService.bond_report_list(query_data=kwargs.get("params")))
