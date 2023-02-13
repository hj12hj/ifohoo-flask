from variables.db_connection import db

"""
    保险收益测算表列sql
"""


class InsuranceProfitCalculationSql:
    def __init__(self):
        self.db = db

    """
    保险收益测算表列表查询
    """

    def get_profit_calculation_report_list(self, query_data):
        total, data = self.db.query_page(
            "select SETTLE_DATE as settleDate, BIZ_TYPE_CODE as bizTypeCode, ASSET_LIAB_TYPE_CODE as assetLiabTypeCode, "
            "SECU_GLOBAL_CODE as secuGlobalCode, SECU_NAME as secuName, SECU_CATEGORY_CODE as secuCategoryCode, "
            "POSITION_CREATE_DATE as positionCreateDate, POSITION_CLEAR_DATE as positionClearDate,"
            "INVE_COST as inveCost,INVE_REAL_PROFIT as inveRealProfit from cost_position_funds where settle_date =:1 and POSITION_QTY >0 ",
            ("2023-02-09",), handle_none=True)
        return {"total": len(data), "list": data}
        # total2, data2 = self.db.query_page(
        #     "select SETTLE_DATE as settleDate, BIZ_TYPE_CODE as bizTypeCode, ASSET_LIAB_TYPE_CODE as assetLiabTypeCode, "
        #     "SECU_GLOBAL_CODE as secuGlobalCode, SECU_NAME as secuName, SECU_CATEGORY_CODE as secuCategoryCode, "
        #     "POSITION_CREATE_DATE as positionCreateDate, POSITION_CLEAR_DATE as positionClearDate,"
        #     "INVE_COST as inveCost,INVE_REAL_PROFIT as inveRealProfit from cost_position_funds "
        #     "where settle_date =:1 and POSITION_QTY = 0 and POSITION_CLEAR_DATE >= '2022-12-31' ",
        #     (query_data.get("settleDate"),), handle_none=True)
        #
        # total3, data3 = self.db.query_page(
        #     "select SETTLE_DATE as settleDate, BIZ_TYPE_CODE as bizTypeCode, ASSET_LIAB_TYPE_CODE as assetLiabTypeCode, "
        #     "SECU_GLOBAL_CODE as secuGlobalCode, SECU_NAME as secuName, SECU_CATEGORY_CODE as secuCategoryCode, "
        #     "POSITION_CREATE_DATE as positionCreateDate, POSITION_CLEAR_DATE as positionClearDate,"
        #     "INVE_COST as inveCost,RECENT_INVE_REAL_PROFIT as inveRealProfit from cost_position_security_invest "
        #     "where settle_date =:1 and POSITION_QTY > 0 and ",
        #     (query_data.get("settleDate"),), handle_none=True)
        #
        # total4, data4 = self.db.query_page(
        #     "select SETTLE_DATE as settleDate, BIZ_TYPE_CODE as bizTypeCode, ASSET_LIAB_TYPE_CODE as assetLiabTypeCode, "
        #     "SECU_GLOBAL_CODE as secuGlobalCode, SECU_NAME as secuName, SECU_CATEGORY_CODE as secuCategoryCode, "
        #     "POSITION_CREATE_DATE as positionCreateDate, POSITION_CLEAR_DATE as positionClearDate,"
        #     "INVE_COST as inveCost,RECENT_INVE_REAL_PROFIT as inveRealProfit from cost_position_security_invest "
        #     "where settle_date =:1 and POSITION_QTY = 0 and POSITION_CLEAR_DATE >= '2022-12-31' ",
        #     (query_data.get("settleDate"),), handle_none=True)




