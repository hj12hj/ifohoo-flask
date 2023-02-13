from variables.db_connection import db

"""
    短期报表列sql
"""


class IncomeCalculationReportSql:
    def __init__(self):
        self.db = db
        # 存款查询
        self.ck_sql = "select organ_code," \
                 "settle_date," \
                 "case when biz_type_code = 'funds_interbank' then '存款' when biz_type_code = 'funds_repurchase' and asset_liab_type_code = 'MRFSZC' then '逆回购' else '' end as productName," \
                 "position_create_date," \
                 "position_clear_date," \
                 "inve_cost," \
                 "position_qty," \
                 "ref_match_net_price," \
                 "ref_settle_date" \
                 " from cost_position_funds" \
                 " where settle_date = '%s' and position_qty > 0 and secu_category_code in ('DDA','DDC','DDN','DDT')"


    """
    短期债券报表列表查询
    """
    def get_income_calculation_report_list(self, query_data):
        #
        organCode = query_data.get("organCode")
        startDate = query_data.get("startDate")
        endDate = query_data.get("endDate")
        day = 365

        ck_start_data = self.db.query_all(self.ck_sql % startDate, None)
        print(ck_start_data)
        ck_end_data = self.db.query_all(self.ck_sql % endDate, None)
        print(ck_end_data)
        data = []
        data1 = {"productName": "存款", "weightedOccupancyAmt": 4109.59, "incomeAmt": 89.73, "interestRate": 2.18,
                 "scaleRatio": 9.16}
        data2 = {"productName": "存款", "weightedOccupancyAmt": 4109.59, "incomeAmt": 89.73, "interestRate": 2.18,
                 "scaleRatio": 9.16}
        data3 = {"productName": "存款", "weightedOccupancyAmt": 4109.59, "incomeAmt": 89.73, "interestRate": 2.18,
                 "scaleRatio": 9.16}
        data4 = {"productName": "存款", "weightedOccupancyAmt": 4109.59, "incomeAmt": 89.73, "interestRate": 2.18,
                 "scaleRatio": 9.16}
        data.append(data1)
        data.append(data2)
        data.append(data3)
        data.append(data4)
        return {"total": len(data), "list": data}
