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
        total, data = self.db.query_page(
            "select * from biz_trade_flow where secu_category_code like :1 and secu_category_code <> :2 and settle_date =:3",
            ("DB%", 'DBN', query_data.get("settleDate"),),
            handle_none=True)
        return {"total": total, "list": data}
