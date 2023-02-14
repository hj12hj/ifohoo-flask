from variables import local_token
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

    def get_funds_list(self,queryData, lastYearEnd):
        organCode = local_token.token_info.get("organCode")
        data = self.db.query_all(
            "select SETTLE_DATE as settleDate, BIZ_AUX_TYPE_CODE as bizTypeCode, ASSET_LIAB_TYPE_CODE as assetLiabTypeCode, " \
            "SECU_GLOBAL_CODE as secuGlobalCode, SECU_NAME as secuName, SECU_CATEGORY_CODE as secuCategoryCode, " \
            "POSITION_QTY as positionQty, POSITION_CREATE_DATE as positionCreateDate, POSITION_CLEAR_DATE as positionClearDate," \
            "INVE_COST as inveCost,INVE_REAL_PROFIT as inveRealProfit from cost_position_funds where  " \
            "organ_Code = ：1 and settle_date =:2 and POSITION_QTY >0 or (POSITION_QTY = 0 and POSITION_CLEAR_DATE >= :3)  ",
            (organCode, queryData, lastYearEnd,))
        return data

    def get_security_invest_list(self,queryData, lastYearEnd):
        organCode = local_token.token_info.get("organCode")
        data = self.db.query_all(
            "select SETTLE_DATE as settleDate, BIZ_TYPE_CODE as bizTypeCode, ASSET_LIAB_TYPE_CODE as assetLiabTypeCode, " \
            "SECU_GLOBAL_CODE as secuGlobalCode, SECU_NAME as secuName, SECU_CATEGORY_CODE as secuCategoryCode, " \
            "POSITION_QTY as positionQty, POSITION_CREATE_DATE as positionCreateDate, POSITION_CLEAR_DATE as positionClearDate," \
            "INVE_COST as inveCost,RECENT_INVE_REAL_PROFIT as inveRealProfit from cost_position_security_invest where  " \
            "organ_Code = ：1 and settle_date =:2 and POSITION_QTY >0 or (POSITION_QTY = 0 and POSITION_CLEAR_DATE >= :3)  ",
            (organCode, queryData, lastYearEnd,))
        return data

    def get_cost_position_data(self,secuGlobalCode, positionClearDate):
        organCode = local_token.token_info.get("organCode")
        data = self.db.query_all(
            "select SETTLE_DATE as settleDate, BIZ_TYPE_CODE as bizTypeCode, ASSET_LIAB_TYPE_CODE as assetLiabTypeCode, " \
            "SECU_GLOBAL_CODE as secuGlobalCode, SECU_NAME as secuName, SECU_CATEGORY_CODE as secuCategoryCode, " \
            "POSITION_QTY as positionQty, POSITION_CREATE_DATE as positionCreateDate, POSITION_CLEAR_DATE as positionClearDate," \
            "INVE_COST as inveCost,RECENT_INVE_REAL_PROFIT as inveRealProfit from cost_position_security_invest where  " \
            "organ_Code = :1 and SECU_CATEGORY_CODE = :2 and POSITION_CLEAR_DATE = :3 and POSITION_QTY = 0  "
            "union all" \
            "select SETTLE_DATE as settleDate, BIZ_TYPE_CODE as bizTypeCode, ASSET_LIAB_TYPE_CODE as assetLiabTypeCode, " \
            "SECU_GLOBAL_CODE as secuGlobalCode, SECU_NAME as secuName, SECU_CATEGORY_CODE as secuCategoryCode, " \
            "POSITION_QTY as positionQty, POSITION_CREATE_DATE as positionCreateDate, POSITION_CLEAR_DATE as positionClearDate," \
            "INVE_COST as inveCost,RECENT_INVE_REAL_PROFIT as inveRealProfit from cost_position_security_invest where  " \
            "organ_Code = :1 and SECU_CATEGORY_CODE = :2 and POSITION_CLEAR_DATE = :3 and POSITION_QTY = 0  ",
            (organCode, secuGlobalCode, positionClearDate,))
        return data





