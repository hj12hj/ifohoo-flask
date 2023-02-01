from aop.handle_sql_result import handle_time_format
from aop.handle_transation import transaction
from variables.db_connection import db

"""
    每日持仓列sql
"""


class CostPositionSql:
    def __init__(self):
        self.db = db

    """
    每日持仓列表查询
    """

    def get_cost_position_list(self, query_data):
        total, data = self.db.query_page("select * from cost_position_security_invest where position_no =:1",
                                         (query_data.get("positionNo"),),
                                         handle_none=True)
        return {"total": total, "list": data}
