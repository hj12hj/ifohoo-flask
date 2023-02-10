from variables.db_connection import db

"""
    短期报表列sql
"""


class IncomeCalculationReportSql:
    def __init__(self):
        self.db = db

    """
    短期债券报表列表查询
    """

    def get_income_calculation_report_list(self, query_data):
        # total, data = self.db.query_page(
        #     "select * from biz_trade_flow where secu_category_code like :1 and secu_category_code <> :2 and settle_date =:3",
        #     ("DB%", 'DBN', query_data.get("settleDate"),),
        #     handle_none=True)
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
