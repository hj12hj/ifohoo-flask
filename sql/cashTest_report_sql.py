import total as total

from variables import local_token
from variables.db_connection import db

"""
    现金流测试报表列sql
"""


class CashTestReportSql:
    def __init__(self):
        self.db = db

    """
    现金流测试报表列表查询
    """

    def get_cashTest_report_list(self, query_data):
        settleDate = query_data.get("settleDate")
        organCode = local_token.token_info.get("organCode")
        total, data = self.db.query_page(
            "select settle_date,secu_category_code,inve_cost,(select due_date from secu_basic where secu_global_code = cost_position_security_invest.secu_global_code) as due_date ,"
            " (select rating_code from secu_rating where secu_global_code = cost_position_security_invest.secu_global_code) as secu_rating_code"
            " from cost_position_security_invest where organ_code=:1 and settle_date =:2 ",
            (organCode, settleDate,),
            handle_none=True)

        return {"total": total, "list": data}
