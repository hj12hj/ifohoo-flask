from aop.handle_sql_result import handle_time_format
from aop.handle_transation import transaction
from variables.db_connection import db


class CostPositionSql:
    def __init__(self):
        self.db = db

    def get_cost_position_list(self, query_data):
        positionNo = query_data.get("positionNo")
        if positionNo is None or positionNo == "":
            positionNo = None

        totle, data = self.db.query_page("select * from COST_POSITION_SECURITY_INVEST where POSITION_NO =:1",
                                         (positionNo,),
                                         handle_none=True)
        return {"totle": totle, "list": data}
