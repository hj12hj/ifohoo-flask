from variables.db_connection import db

"""
    资产明细sql
"""


class AssetDetailReportSql:
    def __init__(self):
        self.db = db

    """
        持仓数据查询
    """

    def get_assetDetail_report_list(self, query_data):
        settleDate = query_data.get("settleDate")
        if settleDate is None or settleDate == "":
            return self.db.query_all(
                "select * from cost_position_security_invest")
        else:
            return self.db.query_all(
                "select secu_category_code, secu_global_code, secu_name, inve_cost,position_create_date as trade_date," \
                "(select due_date from secu_basic where secu_global_code = cost_position_security_invest.secu_global_code) as due_date" \
                " from cost_position_security_invest where settle_date =:1 " \
                "union all" \
                " select secu_category_code, secu_global_code, secu_name, inve_cost, position_create_date as trade_date," \
                "(select due_date from secu_basic where secu_global_code = cost_position_funds.secu_global_code)as due_date" \
                " from cost_position_funds where settle_date =:1",
                (settleDate,))

    """
        持仓数据查询（查询账面余额）
    """

    def get_face_value_list(self, secuGlobalCode, queryDate):
        if queryDate is None or queryDate == "":
            return self.db.query_all(
                "select inve_cost from cost_position_security_invest")
        else:
            return self.db.query_all(
                "select inve_cost from cost_position_funds where secu_global_code =:1 and settle_date =:2 ",
                (secuGlobalCode, queryDate,))
