from variables.db_connection import db

"""
    综合流动比率报表列sql
"""


class FlowRateReportSql:
    def __init__(self):
        self.db = db

    """
    综合流动比率报表列表查询
    """

    def get_flowRate_report_list(self, query_data):
        total, data = self.db.query_page(
            "select * from cost_position_funds where settle_date =:1",
            (query_data.get("settleDate"),),
            handle_none=True)

        return {"total": total, "list": data}
