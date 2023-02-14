from variables import local_token
from variables.db_connection import db

"""
    收益率计算报表列sql
"""


class IncomeCountReportSql:
    def __init__(self):
        self.db = db

    """
    收益率计算报表列表查询
    """

    def get_incomeCount_report_list(self, query_data):
        settleDate = query_data.get("settleDate")
        organCode = local_token.token_info.get("organCode")
        total, data = self.db.query_page(
            "select settle_date,secu_category_code,inve_cost,(select due_date from secu_basic where secu_global_code = cost_position_security_invest.secu_global_code) as due_date "
            " from cost_position_security_invest where organ_code=:1 and settle_date =:2 ",
            (organCode, settleDate,),
            handle_none=True)

        return {"total": total, "list": data}
